# -*- coding: utf-8 -*-

def checkUnderbar(temp_str: str) -> str:
    ret_name = [temp_str[0]]
    for index in range(1, len(temp_str)):
        if temp_str[index - 1] == "_":
            ret_name.append(temp_str[index].upper())
        elif temp_str[index] != "_":
            ret_name.append(temp_str[index])
    return ret_name

def camelCase(name:str) -> str:
    """
    camelCase
    """
    ret_name = checkUnderbar(name)

    ret_name[0] = ret_name[0].lower()
    return ''.join(ret_name)

def pascalCase(name: str) -> str:
    """
    PascalCase
    """
    ret_name = checkUnderbar(name)
    ret_name[0] = ret_name[0].upper()
    return ''.join(ret_name)

def snakeCase(name: str) -> str:
    """
    snake_case
    """
    name = name[0].lower() + name[1:]
    name = list(map(lambda s: '_'+s.lower() if s.isupper() else s, name))
    return ''.join(name)


def test_solution():
    assert camelCase("test_solution") == "testSolution"
    assert camelCase("TestSolution") == "testSolution"

    assert pascalCase("test_solution") == "TestSolution"
    assert pascalCase("testSolution") == "TestSolution"

    assert snakeCase("testSolution") == "test_solution"
    assert snakeCase("TestSolution") == "test_solution"


