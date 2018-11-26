def solution(array):
    d = [0 for x in range(len(array))]
    d[0] = array[0]

    for i in range(1, len(array)):
        d[i] = max(d[i-1] + array[i], array[i])

    maxInt = 0
    for i in d:
        if i > maxInt:
            maxInt = i

    print(maxInt)


solution([-2,1,-3,4,-1,2,1,-5,4])
