import re

import cdmpyparser


def get_module_info(file) -> cdmpyparser.BriefModuleInfo:
    c = cdmpyparser.getBriefModuleInfoFromFile(file)
    return c


def get_all_variables(file_name) -> set:
    # ^\s* - строка начинается с 0 или более пробелов
    # (\w+) - один или более буква, а также цифры и _
    # после знака равно любые символы
    pattern = r'^\s*(?P<variable>\w+) = .+'
    variables = set()
    with open(file_name, 'r') as file:
        for line in file.readlines():
            match = re.search(pattern, line)
            if match:
                variables.add(match.group('variable'))
    return variables
