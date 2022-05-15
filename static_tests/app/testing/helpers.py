from typing import Callable


def search_pattern_with_func(file_list: list, pattern: str,
                             func: Callable) -> bool:
    """
    Search pattern with func in each file from file_list.

    :param file_list: list with files for matching
    :param pattern: pattern for matching
    :param func: function to call
    :return: True if pattern is found, else - False
    """
    for file in file_list:
        if func(file, pattern):
            return True
    return False


def search_with_func(file_list: list, func: Callable, *args, **kwargs) -> bool:
    """
    Calling <func> with args for each file in <file_list> and return result.

    :param file_list: list with files for matching
    :param func: function to call
    :return: True if any called func return True, else - False
    """
    for file in file_list:
        if func(file, *args, **kwargs):
            return True
    return False
