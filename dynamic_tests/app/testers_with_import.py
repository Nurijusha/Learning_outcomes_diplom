import os
import sys

from tester_with_running import TestResult
from logger_utils import get_logger

logger = get_logger(__name__)


def with_custom_dir_and_python_path(func):
    """
    Decorator for setting current directory and PYTHONPATH before running
    testing and after.
    """

    def wrapper(base_dir, *args, **kwargs):
        # Save cwd for future recovering
        cwd = os.getcwd()
        # Set current directory to dir with solutions
        os.chdir(base_dir)
        # Add solutions dir to PYTHONPATH
        sys.path.append(base_dir)

        res = func(base_dir, *args, **kwargs)

        # Recover all settings
        sys.path.remove(base_dir)
        os.chdir(cwd)

        return res

    return wrapper


@with_custom_dir_and_python_path
def testing_module_10_task_1(base_dir: str) -> list[TestResult]:
    try:
        from module_10.task_1_mean_function import mean
    except ImportError:
        return [TestResult(0, False, 'Import error')]

    results = []
    if mean() != 0.0:
        results.append(TestResult(0, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(0, True, 'ACCESS'))

    if mean(7) != 7.0:
        results.append(TestResult(1, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(1, True, 'ACCESS'))

    if mean(1.5, True, ['джфыщкпл'], 'beegeek', 2.5, (1, 2)) != 2.0:
        results.append(TestResult(2, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(2, True, 'ACCESS'))

    if mean(True, ['stop'], 'beegeek', (1, 2)) != 0.0:
        results.append(TestResult(3, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(3, True, 'ACCESS'))

    if mean(-1, 2, 3, 10, ('5')) != 3.5:
        results.append(TestResult(4, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(4, True, 'ACCESS'))

    return results


@with_custom_dir_and_python_path
def testing_module_10_task_2(base_dir: str) -> list[TestResult]:
    try:
        from module_10.task_2_filling_matrix import matrix
    except ImportError:
        return [TestResult(0, False, 'Import error')]

    results = []
    if matrix() != [[0]]:
        results.append(TestResult(0, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(0, True, 'ACCESS'))

    if matrix(3) != [[0, 0, 0], [0, 0, 0], [0, 0, 0]]:
        results.append(TestResult(1, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(1, True, 'ACCESS'))

    if matrix(2, 5) != [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]:
        results.append(TestResult(2, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(2, True, 'ACCESS'))

    if matrix(3, 4, 9) != [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]:
        results.append(TestResult(3, False, 'WRONG ANSWER'))
    else:
        results.append(TestResult(3, True, 'ACCESS'))

    return results
