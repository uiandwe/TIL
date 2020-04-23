def getWays(n, coins):

    d = [0 for _ in range(n+1)]
    d[0] = 1

    for c in coins:
        for i in range(c, n+1):
            d[i] = d[i-c] + d[i]


    print(d[n])


getWays(4, [1, 2, 3])
getWays(10, [2, 5, 3, 6])

