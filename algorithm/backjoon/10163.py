def solution(array):

    d = [[0 for x in range(20)] for y in range(20)]

    rect = 0
    for point in array:
        x1 = point[0]
        y1 = point[1]
        x2 = point[2]
        y2 = point[3]
        rect += 1
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                d[i][j] = rect
    # for i in d:
    #     print(i)

    dict = {}
    for i in range(10):
        for j in range(10):
            val = d[i][j]
            if val != 0:
                if val in dict:
                    dict[val] += 1
                else:
                    dict[val] = 1

    print(dict)


solution([[0, 0, 5, 5], [1, 4, 3, 5]])
solution([[0, 0, 10, 10], [2, 2, 7, 7]])
