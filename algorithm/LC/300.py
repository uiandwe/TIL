# LIS n^2

d = []

def solution(array):
    for i in range(len(array)):
        d.append(1)

    for i in range(1, len(array)):
        max = 0
        for j in range(i):
            if array[j] < array[i] and d[j] > max:
                max = d[j]
        d[i] = max+1

    print(d)


solution([10, 9, 2, 5, 7, 101, 20])
