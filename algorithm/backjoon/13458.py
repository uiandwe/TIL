def solution(testRooms, b, c):
    ret_count = 0
    for i in testRooms:
        i = i - b
        ret_count += 1
        if i > 0:
            if i < c:
                ret_count += 1
            else:
                temp = i // c
                if i % c != 0:
                    temp += 1
                ret_count += temp


    print(ret_count)

solution([1], 1, 1)
solution([3, 4, 5], 2, 2)
solution([10, 9 ,10 ,9 ,10], 7, 2)
solution([1000000, 1000000 ,1000000, 1000000, 1000000], 5, 7)
