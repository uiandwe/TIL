# -*- coding: utf-8 -*-
def solution(progresses, speeds):
    answer = []
    complite = [x for x in progresses]
    q = []

    while progresses:
        for i in range(len(speeds)):
            complite[i] += speeds[i]

        if complite[0] >= 100:
            for i in range(len(complite)):
                if complite and complite[0] >= 100:
                    q.append(progresses)
                    progresses.pop(0)
                    complite.pop(0)
                    speeds.pop(0)
                else:
                    break

        if q:
            answer.append(len(q))
            q = []

    return answer


assert solution([93,30,55], [1,30,5]) == [2, 1]
assert solution([93, 30], [1, 30]) == [2]
assert solution([93], [1]) == [1]
assert solution([30, 93, 55], [30, 1, 5]) == [1, 1, 1]
assert solution([99, 99, 99], [1, 1, 1]) == [3]
assert solution([1, 2, 3], [1, 1, 1]) == [3]
assert solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]) == [1, 2, 3]
assert solution([93, 30, 55, 60, 40, 65], [1, 30, 5, 10, 60, 7]) == [2, 4]


print(solution([93,30,55], [1,30,5]))
# print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5 , 10, 7]))
