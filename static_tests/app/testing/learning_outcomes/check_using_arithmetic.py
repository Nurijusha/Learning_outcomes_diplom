from typing import Callable

from testing.models import LearningOutcome, Recommendation
from testing import parsers


def search_with_func(file_list: list, pattern: str, func: Callable) -> bool:
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


def five(file_list: list):
    recommendations = []
    for operator in ('__truediv__', '__mul__', '__sub__', '__add__'):
        if search_with_func(file_list, operator,
                            parsers.is_exists_overload_arithmetic):
            continue
        recommendations.append(
            Recommendation(
                name=(f'Использует перегрузку арифметических операций: '
                      f'{operator}'),
                task='Модуль 11. Задача 1.'
            )
        )
    return recommendations


def four(file_list: list):
    recommendations = []
    for operator, task in (('-=', 'Модуль 6. Задача 1.'),
                           ('*=', 'Модуль 6. Задача 5.'),
                           ('+=', 'Модуль 6. Задача 2.')):
        if search_with_func(file_list, operator, parsers.is_exists_pattern):
            continue
        recommendations.append(
            Recommendation(
                name=f'Использует сокращенный вид: {operator}',
                task=task
            )
        )
    return recommendations


def three(file_list: list):
    recommendations = []
    for operator in ('%', '//', '**', '/', '*', '-', '+'):
        if search_with_func(file_list, operator, parsers.is_exists_pattern):
            continue
        recommendations.append(
            Recommendation(
                name=f'Использует: {operator}',
                task='Модуль 3. Задача 1.'
            )
        )
    return recommendations


def get_learning_outcome(file_list):
    learning_outcome = LearningOutcome(
        name='Использует арифметические операции',
    )

    if not file_list:
        learning_outcome.score = 2
        return learning_outcome

    for func_score in (five, four, three):
        recommendations = func_score(file_list)
        # If all the criteria of this level are passed
        if not recommendations:
            break
        # If recommendations are exists, add to the learning outcome
        for recommendation in recommendations:
            learning_outcome.recommendations.append(recommendation)
        learning_outcome.score -= 1
    return learning_outcome
