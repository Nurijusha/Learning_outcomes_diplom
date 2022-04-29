"""
Running solutions tests.
"""

import os
import logger_utils

import test_cases as tc
from utils import auto_tests, TestResult

logger = logger_utils.get_logger(__name__)

# { <solution_file> : <test_cases> } for all solutions
TEST_FILE_TEST_CASE = {
    '/module_1/task_1_cezar.py': tc.TEST_CASE_module_1_task_1,
    '/module_1/task_2_compartment_number.py': tc.TEST_CASE_module_1_task_2,
    '/module_2/task_1_identical_numbers.py': tc.TEST_CASE_module_2_task_1,
}


def testing(solutions_dir: str) -> tuple[int, int, int]:
    """
    Return the number of solutions that passed all the tests, tests count
    and the number of timeout.
    :param solutions_dir: path to repo directory with solutions
    :return: ( accepted_solutions , tests_count , timeout_count )
    """
    accepted_solutions = 0
    timeout_count = 0
    for solution_file, test_cases in TEST_FILE_TEST_CASE.items():
        solution_file = solutions_dir + solution_file
        if not os.path.exists(solution_file):
            continue

        results: list[TestResult] = auto_tests(solution_file, test_cases, 15)
        logger.info(results)
        if results:
            # If all test_cases for solution are accepted
            if all(res.accepted for res in results):
                accepted_solutions += 1
            if any(res.comment == 'TIMEOUT' for res in results):
                timeout_count += 1
    return accepted_solutions, len(TEST_FILE_TEST_CASE), timeout_count
