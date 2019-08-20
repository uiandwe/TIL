# -*- coding: utf-8 -*-
import collections

def solution(participant, completion):
    dict = collections.Counter(participant) - collections.Counter(completion)
    return ''.join(dict.keys())


def test_solution():
    assert solution(["leo", "kiki", "eden"], ["eden", "kiki"]) == "leo"
    assert solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]) == "vinko"
    assert solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]) == "mislav"
