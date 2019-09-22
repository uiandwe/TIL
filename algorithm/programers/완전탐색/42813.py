from itertools import permutations
from functools import lru_cache


@lru_cache(maxsize=256)
def is_prime(n: int)-> bool:
    if n < 2:
        return False

    for i in range(2, n):
        if n % i is 0:
            return False
    return True


def solution(numbers):
    answer = 0

    pool = list(numbers)

    permutaion_arr = set()
    for i in range(len(pool)):
        permutaion_arr |= set(map(int, map("".join, permutations(pool, i+1))))
    permutaion_arr -= set(range(0, 2))

    for v in sorted(list(permutaion_arr)):
        if is_prime(v):
            answer += 1
    return answer


def test_solution():
    assert solution("17") == 3
    assert solution("011") == 2




print(solution("17"))
