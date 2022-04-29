"""
Test_cases for dynamic testing of repository.


Name of each test case should be:
            TEST_CASE_module_ + <module_number> + _task_ + <task_number>
            e.g. "TEST_CASE_module_1_task_1" - test case for module 1 task 1
And the test case should be in this format:
            { <example_input> : <expected_output>, }
"""

TEST_CASE_module_1_task_1 = {
    (1, 'bwfusvfupdbftbs'): 'avetruetocaesar',
    (14, 'fsfftsfufksttskskt'): 'rerrfergrweffewewf',
    (25, 'jjjjjjj'): 'kkkkkkk'
}


def generate_test_task_1_2(a):
    return (a - 1) // 4 + 1


TEST_CASE_module_1_task_2 = {
    i: generate_test_task_1_2(i) for i in range(1, 37)
}

TEST_CASE_module_2_task_1 = {
    (114, 223): 'NO',
    (1523, 3678): 'YES',
    (5543, 3455): 'YES',
    (111234, 989897): 'NO',
    (7756, 15167): 'YES',
    (1234, 4321): 'YES',
    (1234, 5678): 'NO',
    (9754, 123): 'NO',
}
