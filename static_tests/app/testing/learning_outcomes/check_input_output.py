from testing.models import LearningOutcome, Recommendation
from testing import parsers
from testing.helpers import search_with_func


def five(file_list: list):
    recommendations = []
    for param, task in (('end', 'Модуль 6. Задача 2.'),
                        ('sep', 'Модуль 3. Задача 1.')):
        if search_with_func(file_list, func=parsers.is_exists_print_with_param,
                            param=param):
            continue
        recommendations.append(
            Recommendation(
                name=f'Использует параметр: {param}',
                task=task
            )
        )
    if not search_with_func(file_list, func=parsers.is_exists_print_f_str):
        recommendations.append(
            Recommendation(
                name=f'Умеет выводить данные в текстовом оформлении',
                task='Модуль 6. Задача 2.'
            )
        )
    return recommendations


def four(file_list: list):
    recommendations = []
    if not search_with_func(file_list,
                            func=parsers.is_exists_print_line_break):
        recommendations.append(
            Recommendation(
                name='Умеет выводить данные с переносом строки',
                task='Модуль 3. Задача 1.'
            )
        )
    if not search_with_func(file_list,
                            func=parsers.is_exists_input_with_prompt):
        recommendations.append(
            Recommendation(
                name='Использует параметр приглашение в input()',
                task='Модуль 3. Задача 1.'
            )
        )
    return recommendations


def three(file_list: list):
    recommendations = []
    for function_name, task in (('input', 'Модуль 4. Задача 1.'),
                                ('print', 'Модуль 4. Задача 1.')):
        if not search_with_func(file_list, func=parsers.is_using_function,
                                function_name=function_name):
            recommendations.append(
                Recommendation(
                    name=f'Умеет реализовывать: {function_name}',
                    task=task
                )
            )
    return recommendations


def get_learning_outcome(file_list):
    learning_outcome = LearningOutcome(
        name='Умеет реализовывать ввод-вывод данных',
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
