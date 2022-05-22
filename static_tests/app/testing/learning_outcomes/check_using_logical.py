from testing.models import LearningOutcome, Recommendation
from testing.helpers import search_with_func
from testing import parsers


def five(file_list: list):
    if search_with_func(
            file_list,
            parsers.is_exist_multiple_logical_ops_in_one_expression):
        return []
    return [
        Recommendation(
            name='Использует сложные логические операции',
            task='Модуль 1. Задача 1.'
        )
    ]


def four(file_list: list):
    recommendations = []
    for operator, task in (('not', 'Модуль 10. Задача 2.'),
                           ('and', 'Модуль 10. Задача 2.'),
                           ('or', 'Модуль 1. Задача 1.')):
        if search_with_func(file_list, operator=operator,
                            func=parsers.is_exists_logic_operator):
            continue
        recommendations.append(
            Recommendation(
                name=f'Использует логическую операцию: {operator}',
                task=task
            )
        )
    return recommendations


def three(file_list: list):
    recommendations = []
    for operator, task in (('<|>', 'Модуль 4. Задача 1.'),
                           ('>=|<=', 'Модуль 4. Задача 1.'),
                           ('!=', 'Модуль 7. Задача 1.'),
                           ('==', 'Модуль 6. Задача 1.')):
        if search_with_func(file_list, operator=operator,
                            func=parsers.is_exists_logic_operator):
            continue
        recommendations.append(
            Recommendation(
                name=f'Использует логический оператор: {operator}',
                task=task
            )
        )
    return recommendations


def get_learning_outcome(file_list):
    learning_outcome = LearningOutcome(
        name='Использует логические операции',
    )

    if not file_list:
        learning_outcome.score = 2
        return learning_outcome

    for func_score in (five,):  # , four, three):
        recommendations = func_score(file_list)
        # If all the criteria of this level are passed
        if not recommendations:
            break
        # If recommendations are exists, add to the learning outcome
        for recommendation in recommendations:
            learning_outcome.recommendations.append(recommendation)
        learning_outcome.score -= 1
    return learning_outcome
