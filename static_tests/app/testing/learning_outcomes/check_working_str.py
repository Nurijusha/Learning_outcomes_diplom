from testing.models import LearningOutcome, Recommendation
from testing import parsers
from testing.helpers import search_with_func


def five(file_list: list):
    if search_with_func(
            file_list,
            func=parsers.is_using_function, function_name='ord|chr'):
        return []
    return [
        Recommendation(
            name='Понимает как хранится строка в памяти: использует ord() или'
                 'chr()',
            task='Модуль 4. Задача 1.'
        )
    ]


def four(file_list: list):
    recommendations = []
    for method_name, task in (('replace', 'Модуль 10. Задача 8.'),
                              ('find', 'Модуль 4. Задача 3.'),
                              ('lower|upper', 'Модуль 4. Задача 2.'),
                              ('split|join', 'Модуль 6. Задача 2.')):
        if search_with_func(file_list, func=parsers.is_using_method,
                            method_name=method_name):
            continue
        recommendations.append(
            Recommendation(
                name=f'Использует методы: {method_name}',
                task=task
            )
        )
    if not search_with_func(file_list, func=parsers.is_exist_slices):
        recommendations.append(
            Recommendation(
                name='Умеет брать срезы',
                task='Модуль 10. Задача 5.'
            )
        )
    return recommendations


def three(file_list: list):
    recommendations = []
    if not search_with_func(file_list,
                            func=parsers.is_exists_str_iteration):
        recommendations.append(
            Recommendation(
                name='Использует итерирование строк',
                task='Модуль 4. Задача 1.'
            )
        )
    if not search_with_func(file_list, func=parsers.is_exists_indexing):
        recommendations.append(
            Recommendation(
                name='Использует индексацию',
                task='Модуль 4. Задача 1.'
            )
        )
    if not search_with_func(file_list, func=parsers.is_exists_getting_length):
        recommendations.append(
            Recommendation(
                name='Умеет узнавать длину строки',
                task='Модуль 10. Задача 5.'
            )
        )
    if not search_with_func(file_list,
                            func=parsers.is_exists_creating_str):
        recommendations.append(
            Recommendation(
                name='Умеет создавать строку',
                task='Модуль 4. Задача 1.'
            )
        )
    return recommendations


def get_learning_outcome(file_list):
    learning_outcome = LearningOutcome(
        name='Умеет работать со строками',
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
