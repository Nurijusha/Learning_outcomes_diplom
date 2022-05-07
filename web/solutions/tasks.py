import requests
import logging

from celery import shared_task, states
from celery.result import AsyncResult
from celery.exceptions import Ignore

from .models import Solution, LearningOutcome, SolutionTesting

logger = logging.getLogger(__name__)


def create_save_learning_outcome(solution: Solution, name: str, score: int):
    learning_outcome = LearningOutcome(
        solution=solution,
        name=name,
        score=score
    )
    logger.info(f'Create new Learning Outcome ({learning_outcome}) for '
                f'Solution ({solution})')
    learning_outcome.save()


def check_set_status_solution_testing(dynamic_test_task_id: str = None,
                                      static_test_task_id: str = None,
                                      status: str = 'SUCCESS'):
    """
    Check dynamic and static testing celery tasks states for received
    SolutionTesting (getting with one of ids) and set status.
    If any celery task FAILURE -> status = FAILURE.
    If any celery task STARTED -> status = STARTED.
    If all celery tasks SUCCESS -> status = SUCCESS.

    If received status other than 'SUCCESS' -> set SolutionCeleryTask for it.
    """
    if dynamic_test_task_id:
        solution_testing = SolutionTesting.objects.get(
            dynamic_test_task_id=dynamic_test_task_id
        )
        if not solution_testing.static_test_task_id:
            solution_testing.status = status
            solution_testing.save()
            return
    else:
        solution_testing = SolutionTesting.objects.get(
            static_test_task_id=static_test_task_id
        )
        if not solution_testing.dynamic_test_task_id:
            solution_testing.status = status
            solution_testing.save()
            return

    if status != 'SUCCESS':
        solution_testing.status = status
        solution_testing.save()
        return
    if solution_testing.status != 'STARTED':
        return

    dt_task_state = AsyncResult(solution_testing.dynamic_test_task_id).state
    st_task_state = AsyncResult(solution_testing.static_test_task_id).state

    if any(state == 'FAILURE' for state in (dt_task_state, st_task_state)):
        new_status = 'FAILURE'
    elif any(state == 'STARTED' for state in (dt_task_state, st_task_state)):
        new_status = 'STARTED'
    elif all(state == 'SUCCESS' for state in (dt_task_state, st_task_state)):
        new_status = 'SUCCESS'
    else:
        new_status = 'UNKNOWN'
    solution_testing.status = new_status
    solution_testing.save()


def set_task_state(task: shared_task, state: str = states.FAILURE):
    """
    Set task state and solution_celery_task status to <state> parameter.

    :param task: shared_task object
    :param state: new state for task. Default - FAILURE
    :return: None
    """
    task.update_state(state=state)
    check_set_status_solution_testing(
        dynamic_test_task_id=task.request.id,
        status=state
    )


@shared_task(bind=True)
def dynamic_testing(self, github_url: str, solution_id: int):
    """
    Running dynamic testing. Save resulting learning outcomes.
    """
    solution = Solution.objects.filter(id=solution_id).first()
    # If solution deleted from other task
    if not solution:
        set_task_state(self)
        # Without this raise, task state will be set to SUCCESS
        raise Ignore()

    try:
        payload = {'github_url': github_url}
        # Run dynamic testing
        response = requests.get('http://dynamic-tests:6000/do-tests',
                                json=payload,
                                timeout=360)
        response = response.json()
        if response.get('result') == 'error':
            set_task_state(self)
            raise Ignore()
        create_save_learning_outcome(
            solution,
            'Умеет писать работоспособный код',
            int(response.get('result')))
        create_save_learning_outcome(
            solution,
            ('Соблюдает время работы программы,указанное в требованиях к '
             'задачам'),
            int(response.get('access_time'))
        )
        check_set_status_solution_testing(
            dynamic_test_task_id=self.request.id)
    except Exception as e:
        logger.error(e)
        # Delete solution, because testing Failed
        solution.delete()
        set_task_state(self)
        raise Ignore()
