def solution(array):
    d = [0 for x in range(len(array))]
    d[0] = array[0]


    for i in range(1, len(array)):
        d[i] = max(array[i], array[i]+d[i-1])

    print(max(d))


solution([-2,1,-3,4,-1,2,1,-5,4])
solution([4, -1, 2, 1])
