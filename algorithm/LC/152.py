def solution(array):
    d = [[0 for x in range(2)] for y in array]
    d[0][0] = array[0]
    d[0][1] = array[0]

    for i in range(1, len(array)):
        c = array[i]
        d[i][0] = max(c, c*d[i-1][0], c*d[i-1][1])
        d[i][1] = min(c, c*d[i-1][0], c*d[i-1][1])

    print(d)


# solution([2, 3, -2, 4])
solution([-2, 0, -1])


def solution1(array):
    d = [0 for x in array]
    d[0] = array[0]

    for i in range(1, len(array)):
        d[i] = max(array[i], array[i]+array[i-1])

    print(d)


solution1([2, 3, -5, 4])
