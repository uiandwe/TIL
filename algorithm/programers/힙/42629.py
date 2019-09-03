# -*- coding: utf-8 -*-
import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    heap_list = []
    index = 0
    while stock < k:
        for i in range(index, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(heap_list, (-supplies[i], supplies[i]))
                index = i+1
            else:
                break

        stock += heapq.heappop(heap_list)[1]
        answer += 1
    return answer


def test_solution():
    assert solution(4, [4,10,15], [20,5,10], 30) == 2
    assert solution(5, [1, 2, 3, 4, 5], [1, 1, 1, 1, 25], 30) == 1
    assert solution(4, [1, 2, 3, 4, 5], [1, 1, 1, 1, 25], 30) == 2
    assert solution(3, [1, 2, 3, 4, 5], [1, 1, 1, 1, 25], 30) == 3
    assert solution(10, [1, 10], [5, 100], 110) == 1
    assert solution(4, [1, 2, 3, 4], [10, 40, 30, 20], 100) == 4
    assert solution(4, [4, 10, 15], [7, 5, 14], 30) == 3

solution(4, [4,10,15], [20,5,10], 30)
