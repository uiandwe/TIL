def solutioin(coin, money):
    d = [0 for x in range(money+1)]
    d[0] = 1

    for c in coin:
        for i in range(money+1):
            if i-c >= 0:
                d[i] = d[i-c]+d[i]

    print(d[money])


solutioin([5, 7], 22)
solutioin([1, 2], 1000)
solutioin([1, 5, 10], 100)
