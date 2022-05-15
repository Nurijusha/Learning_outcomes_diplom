import re


def is_exists_overload_arithmetic(file_name: str, operator: str) -> bool:
    """
    Search overloading arithmetic operators.

    :param file_name: str of the file for matching
    :param operator: operator
    :return: True if find, else - False
    """
    # ^\s* - строка начинается с 0 или более пробелов
    # def __truediv__ (self, other): - перегрузка
    pattern = fr'^\s*def {operator}\(self, other\):\s*$'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exists_pattern(file_name: str, pattern: str) -> bool:
    """
    Search pattern in file.
    Final pattern for matching: fr'^\s*\w+\s*\{pattern}\s*\w+'.

    :param file_name: str of the file for matching
    :param pattern: pattern for searching
    :return: True if pattern is exists in file, else - False
    """
    # ^\s* - строка начинается с 0 или более пробелов
    # \w+ - любой символ, котороый может быть переменной (буквы, цифры и _)
    pattern = fr'^\s*\w+\s*\{pattern}\s*\w+'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exist_multiple_logical_ops_in_one_expression(file_name: str) -> bool:
    """
    Search using multiple logical operations in one expression in <file_name>.

    :param file_name: str of the file for matching
    :return: True if multiple logical operations in one expression are exist,
    else - False
    """
    # ^[^#\'\"\n]* - строка начинается с любого символа кроме этих
    # (?:or|and|not|>|<|>=|<=|!=|==) - комбинация из двух операторов
    # (между ними любые символы кроме переноса строки .+)
    pattern = (r'^[^#\'\"\n]*(?:or|and|not|>|<|>=|<=|!=|==).+'
               r'(?:or|and|not|>|<|>=|<=|!=|==)[^\'\"\n]+$')
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_using_function(file_name: str, function_name: str) -> bool:
    """
    Search using function with <function_name> in <file_name>.

    :param file_name: str of the file for matching
    :param function_name: name of the function to search
    :return: True if <function_name> function is using, else - False
    """
    pattern = fr'^[^#\'\"\n]*{function_name}\(.+\).*$'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_using_method(file_name: str, method_name: str) -> bool:
    """
    Search using <method_name> method in <file_name> [.method_name()].

    :param file_name: str of the file for matching
    :param method_name: name of the method to search
    :return: True if <method_name> method is using, else - False
    """
    pattern = fr'^[^#\'\"\n]*\w+.{method_name}\(.+\).*$'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exist_slices(file_name: str) -> bool:
    """
    Search using string/list slices.

    :param file_name:str of the file for matching
    :return:True if slices are exist, else - False
    """
    pattern = fr'^[^#\'\"\n]*\w+\[\d*:\d*].*$'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exists_str_iteration(file_name: str) -> bool:
    """
    Search using string iteration.

    :param file_name:str of the file for matching
    :return:True if using string iteration is exists, else - False
    """
    pattern = fr'^[^#\'\"\n]*for \w+ in range\(len\(\w+\)\).*$'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exists_indexing(file_name: str) -> bool:
    """
    Search using string/list indexing.

    :param file_name: str of the file for matching
    :return: True if using string indexing is exists, else - False
    """
    pattern = fr'^[^#\'\"\n]*(\w+\[\d+]).*$'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exists_getting_length(file_name: str) -> bool:
    """
    Search using len().

    :param file_name: str of the file for matching
    :return: True if using len() is exists, else - False
    """
    pattern = fr'^[^#\'\"\n]*(len\(\w+\)).*$'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exists_creating_str(file_name: str) -> bool:
    """
    Search creating string. With input or ' or ".

    :param file_name: str of the file for matching
    :return: True if creating string is exists, else - False
    """
    pattern = fr'^[^#\'\"\n]*\w+ = (input\(|\'|\").*$'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exists_print_with_param(file_name: str, param: str) -> bool:
    """
    Search printing with <param> 'end' or 'sep'.

    :param file_name: str of the file for matching
    :param param: param in print(). end or sep.
    :return: True if printing with param is exists, else - False
    """
    pattern = fr'^[^#\'\"\n]*print\([^)]*\s*{param} ?= ?.+\)$'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exists_print_f_str(file_name: str) -> bool:
    """
    Search printing f-strings.

    :param file_name: str of the file for matching
    :return: True if printing f-string is exists, else - False
    """
    pattern = r'^[^#\'\"\n]*print\(f[\'\"]+.+\)$'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exists_print_line_break(file_name: str) -> bool:
    """
    Search printing string with \\\\n.

    :param file_name: str of the file for matching
    :return: True if printing string with \\n is exists, else - False
    """
    # ^[^#\'\"\n]*print\(.* - строка начинается с print(и любого символа
    # [\'\"]{1}.*\\n.*[\'\"]{1} - открывающая кавычка, \n, закрывающая кавычка
    # .*\)$ - любые символы 0 или более, скобки зыкрываются
    pattern = r'^[^#\'\"\n]*print\(.*[\'\"]{1}.*\\n.*[\'\"]{1}.*\)$'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exists_input_with_prompt(file_name: str) -> bool:
    """
    Search input() with prompt - input(prompt).

    :param file_name: str of the file for matching
    :return: True if input with prompt is exists, else - False
    """
    # ^[^#\'\"\n]*\w+ - строка начинается с переменной
    #  ?= ? - знак равно с двух сторон пробелы либо есть, либо нет
    # input\([\'\"]\w+.*[\'\"]\) - input(), внутри в кавычках строка
    pattern = r'^[^#\'\"\n]*\w+ ?= ?input\([\'\"]\w+.*[\'\"]\)'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exists_iteration_through_nested_list(file_name: str) -> bool:
    """
    Search iteration through a nested list.

    :param file_name: str of the file for matching
    :return: True if iteration is exists, else - False
    """
    # for (?P<element1>\b\w+) in \w+: - итерация по объекту (for el1 in list:)
    # for \w+ in (?P=element1) - итерация по вложенному объекту с именем
    # (for el2 in el1)
    pattern1 = (r'^[^#\'\"\n]*for (?P<element1>\b\w+) in \w+: '
                r'for \w+ in (?P=element1)')
    pattern2 = (r'^[^#\'\"\n]*for \w+ in range\(\w+\):\s*'
                r'for \w+ in range\(\w+\):')
    with open(file_name, 'r') as file:
        f = file.read()
        match1 = re.findall(pattern1, f, flags=re.MULTILINE)
        match2 = re.findall(pattern2, f, flags=re.MULTILINE)
        if match1 or match2:
            return True
    return False


def is_exists_indexing_nested_list(file_name: str) -> bool:
    """
    Search indexing nested list. list1[1][2].

    :param file_name: str of the file for matching
    :return: True if indexing is exists, else - False
    """
    # \w+\[\d+\]\[\d+\] - переменная[позиция][позиция]
    pattern = r'^[^#\'\"\n]*\w+\[\d+\]\[\d+\]'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exists_creating_nested_list(file_name: str) -> bool:
    """
    Search creating nested list. list1 = [[]] or with iteration.

    :param file_name: str of the file for matching
    :return: True if creating nested list is exists, else - False
    """
    # matrix = [[]]
    pattern1 = r'^[^#\'\"\n]*\w+ ?= ?\[.*\[.*\].*\]'
    # for i in range(n):
    #     matrix.append([])
    #     for j in range(m):
    #         matrix[i].append(counter)
    pattern2 = (r'^[^#\'\"\n]*for (?P<element1>\b\w+) in range\(\w+\):\s*'
                r'(?P<matrix>\b\w+).append\(\[\]\)\s*'
                r'for \w+ in range\(\w+\):\s*'
                r'(?P=matrix)\[(?P=element1)\].append\(\w+\)')
    with open(file_name, 'r') as file:
        f = file.read()
        match1 = re.findall(pattern1, f, flags=re.MULTILINE)
        match2 = re.findall(pattern2, f, flags=re.MULTILINE)
        if match1 or match2:
            return True
    return False


def is_exists_list_expression(file_name: str) -> bool:
    """
    Search list expressions. for i in list.

    :param file_name: str of the file for matching
    :return: True if list expression is exists, else - False
    """
    pattern = r'^[^#\'\"\n]*for \w+ in \w+'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exists_del_list(file_name: str) -> bool:
    """
    Search for deleting a list item. del list1[1]

    :param file_name: str of the file for matching
    :return: True if list item deleting is exists, else - False
    """
    pattern = r'^[^#\'\"\n]*del \w+\[\w+\]'
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exists_creating_list(file_name: str) -> bool:
    """
    Search creating list.

    :param file_name: str of the file for matching
    :return: True if list creating is exists, else - False
    """
    # list1 = [] or list1 = [<any_symbols>]
    pattern1 = r'^[^#\'\"\n]*\w+ ?= ?\[.*\]$'
    # list1 = var.split() or list1 = input().split()
    pattern2 = r'^[^#\'\"\n]*\w+ ?= ?[\w()]+.split\(.*\)$'
    with open(file_name, 'r') as file:
        f = file.read()
        match1 = re.findall(pattern1, f, flags=re.MULTILINE)
        match2 = re.findall(pattern2, f, flags=re.MULTILINE)
        if match1 or match2:
            return True
    return False


def is_exists_generator_of_sets(file_name: str) -> bool:
    """
    Search generator of sets. {c for c in iterable_object}.

    :param file_name: str of the file for matching
    :return: True if generator of sets is exists, else - False
    """
    pattern = (r'^[^#\'\"\n]*\w+ ?= ?\{(?P<element>\b\w+) '
               r'for (?P=element) in \w+}')
    with open(file_name, 'r') as file:
        match = re.findall(pattern, file.read(), flags=re.MULTILINE)
        if match:
            return True
    return False


def is_exists_creating_set(file_name: str) -> bool:
    """
    Search creating set. set() or set(<iterable_object>) or {}.

    :param file_name: str of the file for matching
    :return: True if creating set is exists, else - False
    """
    pattern1 = r'^[^#\'\"\n]*set\(\w*\)'
    pattern2 = r'^[^#\'\"\n]*\{.*\}'
    with open(file_name, 'r') as file:
        f = file.read()
        match1 = re.findall(pattern1, f, flags=re.MULTILINE)
        match2 = re.findall(pattern2, f, flags=re.MULTILINE)
        if match1 or match2:
            return True
    return False
