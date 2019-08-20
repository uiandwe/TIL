# -*- coding: utf-8 -*-

def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


def test_solution():
    assert solution(["119", "97674223", "1195524421"]) == False
    assert solution(["123","456","789"]) == True
    assert solution(["12","123","1235","567","88"]) == False

