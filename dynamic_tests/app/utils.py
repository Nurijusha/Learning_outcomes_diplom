import sys
from subprocess import PIPE, TimeoutExpired, run
from collections import namedtuple

TestResult = namedtuple('TestResult', 'number accepted comment')


def get_text_from_case(test_iter: tuple | list) -> str:
    """
    Return raw string from iterable object to pass to the subprocess input
    or output.
    :param test_iter: iterable object with lines for script`s stdin
    :return: e.g. "2\n3\n4\n"
    """
    return '\n'.join(str(s) for s in test_iter)


def run_test(solution_file: str, test_input: str, expected: str,
             timeout: int = 15) -> tuple[bool, str]:
    """
    Run test case for solution with stdin parameters.
    :param solution_file: path of .py file with solution
    :param test_input: input string for stdin
    :param expected: expected result from solution
    :param timeout: time to complete the solution
    :return: bool (ok solution or no) and comment ('ACCEPT', 'WRONG ANSWER',
    'TIMEOUT', 'ERROR')
    """
    try:
        proc = run(
            [sys.executable, solution_file],
            input=test_input,
            stdout=PIPE,
            stderr=PIPE,
            timeout=timeout,
            encoding='utf-8'
        )
    except TimeoutExpired:
        return False, 'TIMEOUT'

    if proc.returncode:
        return False, 'ERROR'

    if str(proc.stdout.strip()) == str(expected):
        return True, 'ACCESS'
    else:
        return False, 'WRONG ANSWER'


def auto_tests(solution_file: str, test_cases: dict, timeout: int):
    """
    Run all test_cases for <solution_file> and return results [ TestResult() ]
    :param solution_file: path of .py file with solution
    :param test_cases: test cases dict { input : expected }
    :param timeout: timeout for solution execution
    :return:
    """
    results = []
    for i, test in enumerate(test_cases.items()):
        _input, expected = test
        # Prepare input string
        if isinstance(_input, (tuple, list)):
            _input = get_text_from_case(_input)
        else:
            _input = str(_input)

        # Prepare output string
        if isinstance(expected, (tuple, list)):
            expected = get_text_from_case(expected)

        accepted, comment = run_test(solution_file, _input, expected, timeout)
        results.append(TestResult(i, accepted, comment))
        if comment == 'TIMEOUT':
            break
    return results
