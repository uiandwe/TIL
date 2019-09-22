# -*- coding: utf-8 -*-
# https://comdoc.tistory.com/entry/34-%EB%8F%99%EC%A0%81-%EA%B3%84%ED%9A%8D%EB%B2%95-%EB%A7%89%EB%8C%80%EA%B8%B0-%EC%9E%90%EB%A5%B4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

def solution(n):
    # size per price
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    r = [0 for i in range(n+1)]

    for i in range(1, n+1):
        max_val = 0
        for j in range(0, i):
            print(p[i-j], r[j])
            max_val = max(max_val, p[i-j] + r[j])
        r[i] = max_val

    return r[n]

def test_solution():
    assert solution(1) == 1
    assert solution(2) == 5
    assert solution(4) == 10
    assert solution(10) == 30
    assert solution(8) == 22

print(solution(4))
