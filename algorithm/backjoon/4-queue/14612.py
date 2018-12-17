
def solution(array):
    queueArr = []
    for order in array:
        if order[0] == 'o':
            queueArr.append([order[1], order[2]])
        elif order[0] == 's':
            queueArr = sorted(queueArr, key=lambda x:x[1])
        else:
            endCook = order[1]
            for index in range(len(queueArr)):
                if queueArr[index][0] == endCook:
                    queueArr.pop(index)
                    break
        print("-------")
        for p in queueArr:
            print(p[0])




solution([['o', 1, 4], ['o', 2, 2], ['o', 3, 3, ], ['s'], ['c', 3], ['c', 2], ['c', 1]])
