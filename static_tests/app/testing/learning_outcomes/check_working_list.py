from testing.models import LearningOutcome, Recommendation
from testing import parsers
from testing.helpers import search_with_func


def five(file_list: list):
    recommendations = []
    if not search_with_func(file_list, func=parsers.is_exists_pattern,
                            pattern=r'.ljust\(|.rjust\('):
        recommendations.append(
            Recommendation(
                name=f'Умеет использовать функции ljust() или rjust()',
                task='Модуль 6. Задача 2.'
            )
        )
    if not search_with_func(
            file_list,
            func=parsers.is_exists_iteration_through_nested_list):
        recommendations.append(
            Recommendation(
                name=f'Умеет перебирать элементы вложенных списков',
                task='Модуль 6. Задача 2.'
            ))
    if not search_with_func(file_list, func=parsers.is_using_function,
                            function_name='min|max|len'):
        recommendations.append(
            Recommendation(
                name=(f'Использует функции min() или max(), или len() со '
                      f'вложенными списками'),
                task='Модуль 6. Задача 4.'
            ))
    if not search_with_func(file_list, parsers.is_exists_indexing_nested_list):
        recommendations.append(
            Recommendation(
                name=f'Использует индексацию с вложенными списками',
                task='Модуль 6. Задача 2.'
            ))
    if not search_with_func(file_list, parsers.is_exists_creating_nested_list):
        recommendations.append(
            Recommendation(
                name=f'Умеет создавать вложенные списки',
                task='Модуль 6. Задача 2.'
            ))
    return recommendations


def four(file_list: list):
    recommendations = []
    if not search_with_func(file_list,
                            func=parsers.is_exists_list_expression):
        recommendations.append(
            Recommendation(
                name='Использует списочные выражения',
                task='Модуль 6. Задача 2.'
            ))
    if not search_with_func(file_list,
                            func=parsers.is_exists_del_list):
        recommendations.append(
            Recommendation(
                name='Умеет удалять элементы - del',
                task='Модуль 6. Задача 5.'
            ))
    if not search_with_func(file_list, func=parsers.is_using_method,
                            method_name='extend'):
        recommendations.append(
            Recommendation(
                name='Умеет расширять списки - extend',
                task='Модуль 6. Задача 5.'
            ))
    if not search_with_func(file_list, func=parsers.is_using_method,
                            method_name='insert'):
        recommendations.append(
            Recommendation(
                name='Умеет добавлять элементы в списки - insert',
                task='Модуль 6. Задача 5.'
            ))
    if not search_with_func(file_list, func=parsers.is_using_method,
                            method_name='append'):
        recommendations.append(
            Recommendation(
                name='Умеет добавлять элементы в списки - append',
                task='Модуль 6. Задача 2.'
            ))
    return recommendations


def three(file_list: list):
    recommendations = []
    if not search_with_func(file_list, func=parsers.is_exist_slices):
        recommendations.append(
            Recommendation(
                name=f'Использует срезы',
                task='Модуль 4. Задача 2.'
            ))
    if not search_with_func(file_list, func=parsers.is_exists_indexing):
        recommendations.append(
            Recommendation(
                name=f'Использует индексацию',
                task='Модуль 6. Задача 1.'
            ))
    if not search_with_func(file_list, func=parsers.is_exists_getting_length):
        recommendations.append(
            Recommendation(
                name=f'Умеет узнавать длину списка',
                task='Модуль 6. Задача 2.'
            ))
    if not search_with_func(file_list, func=parsers.is_exists_creating_list):
        recommendations.append(
            Recommendation(
                name=f'Умеет создавать списки',
                task='Модуль 10. Задача 5.'
            ))
    return recommendations


def get_learning_outcome(file_list):
    learning_outcome = LearningOutcome(
        name='Умеет работать со списками и воспроизводит операции над ними',
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
