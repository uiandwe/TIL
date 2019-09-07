# -*- coding: utf-8 -*-

def checkUnderbar(temp_str: str) -> list:
    first, *others = temp_str.split("_")
    return [first, *map(str.title, others)]

def camelCase(name:str) -> str:
    """
    camelCase
    """
    ret_name = checkUnderbar(name)
    first = ret_name[0]
    ret_name[0] = first[0].lower() + first[1:]
    return ''.join(ret_name)

def pascalCase(name: str) -> str:
    """
    PascalCase
    """
    ret_name = checkUnderbar(name)
    first = ret_name[0]
    ret_name[0] = first[0].upper() + first[1:]
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
    assert camelCase("testSolution") == "testSolution"

    assert pascalCase("test_solution") == "TestSolution"
    assert pascalCase("testSolution") == "TestSolution"
    assert pascalCase("TestSolution") == "TestSolution"

    assert snakeCase("testSolution") == "test_solution"
    assert snakeCase("TestSolution") == "test_solution"
    assert snakeCase("test_solution") == "test_solution"


print(pascalCase("testSolution"))
