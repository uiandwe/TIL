# -*- coding: utf-8 -*-
def solution(progresses, speeds):
    answer = []

    while progresses:
        progresses = [sum([i, j]) for i, j in zip(progresses, speeds)]

        if progresses[0] >= 100:
            end = 0
            remove_index = []
            for index, val in enumerate(progresses):
                if val >= 100:
                   end += 1
                   remove_index.append(index)
                else:
                    break
            answer.append(end)

            for i, index in enumerate(remove_index):
                progresses.pop(index-i)
                speeds.pop(index-i)

    return answer


def test_solution():
    assert solution([93,30,55], [1,30,5]) == [2, 1]
    assert solution([93, 30], [1, 30]) == [2]
    assert solution([93], [1]) == [1]
    assert solution([30, 93, 55], [30, 1, 5]) == [1, 1, 1]
    assert solution([99, 99, 99], [1, 1, 1]) == [3]
    assert solution([1, 2, 3], [1, 1, 1]) == [3]
    assert solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]) == [1, 2, 3]
    assert solution([93, 30, 55, 60, 40, 65], [1, 30, 5, 10, 60, 7]) == [2, 4]


print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5 , 10, 7]))
