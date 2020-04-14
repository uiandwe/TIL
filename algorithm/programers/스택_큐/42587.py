# -*- coding: utf-8 -*-

def solution(priorities, location):
    answer = 1
    priorities = [(index, val) for index, val in enumerate(priorities)]

    while priorities:

        max_val = max(map(lambda x: x[1], priorities))
        if priorities[0][1] != max_val:
            while max_val != priorities[0][1]:
                p = priorities.pop(0)
                priorities.append(p)

        t = priorities.pop(0)

        if t[0] == location:
            break

        answer += 1

    return answer


assert solution([2, 1, 3, 2], 2) == 1
assert solution([1, 1, 9, 1, 1, 1], 0) == 5
assert solution([1], 0) == 1

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
