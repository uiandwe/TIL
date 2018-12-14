import heapq

def solution(array):
    array = sorted(array, key=lambda x: x[0])
    a = []

    for i in range(len(array)):
        first = array[i][0]
        heapq.heappush(a, array[i][1])
        while first < len(a):
            heapq.heappop(a)

    total_sum = 0
    while len(a) > 0:
        total_sum += heapq.heappop(a)

    print(total_sum)

solution([[1, 6], [1, 7], [3, 2], [3, 1], [2, 4], [2, 5], [6, 1]])
solution([[2, 20], [2, 25], [2, 30]])
