# -*- coding: utf-8 -*-

def checkUnderbar(temp_str: str, func_name: str) -> list:
    first, *others = temp_str.split("_")
    first = getattr(first[0], func_name)() + first[1:]
    return ''.join([first, *map(str.title, others)])

def camelCase(name:str) -> str:
    """
    camelCase
    """
    return checkUnderbar(name, 'lower')

def pascalCase(name: str) -> str:
    """
    PascalCase
    """
    return checkUnderbar(name, 'upper')

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
    assert camelCase("testSolution") == "testSolution"

    assert pascalCase("test_solution") == "TestSolution"
    assert pascalCase("testSolution") == "TestSolution"
    assert pascalCase("TestSolution") == "TestSolution"

    assert snakeCase("testSolution") == "test_solution"
    assert snakeCase("TestSolution") == "test_solution"
    assert snakeCase("test_solution") == "test_solution"

camelCase("test_solution")
