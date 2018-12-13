def solution(jewel, bag):
    jewel = sorted(jewel, key=lambda x:x[1], reverse=True)

    bag = sorted(bag)
    putJ = [0 for x in range(len(jewel))]
    totalSum = 0

    for b in bag:
        for i in range(len(jewel)):
            if putJ[i] == 0 and b >= jewel[i][0]:
                putJ[i] = 1
                totalSum += jewel[i][1]
                break

    print(totalSum)


solution([[1, 65], [5, 23], [2, 99]], [10, 2])
solution([[1, 1], [1, 2], [2, 99]], [1])

# 갯수에서 시간초과 / 수정할 필요 
