def solution(money, array):
    d = [0 for x in range(money+1)]

    for i in array:
        for j in range(i, money+1):
            if j - i >= 0:
                d[j] = d[j-i]+1

    print(d[money])


solution(10, [1,5])
solution(420, [1,5,10,50,100,500,1000,5000,10000,50000])
solution(4790, [1,5,10,50,100,500,1000,5000,10000,50000])
