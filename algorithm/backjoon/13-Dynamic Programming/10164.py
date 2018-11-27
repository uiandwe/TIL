

def createMap(x, y):

    d = []
    for i in range(x):
        temp = []
        for j in range(y):
            if i == 0 or j == 0:
                temp.append(1)
            else:
                temp.append(0)
        d.append(temp)

    for i in range(1, x):
        for j in range(1, y):
            d[i][j] = d[i-1][j] + d[i][j-1]

    return d[x-1][y-1]



def solution(n, m, k):
    i = int(k/m)
    j = k%m
    print(createMap(i+1, j) * createMap(n-i, (m-j)+1))



solution(3, 5, 8)
solution(3, 3, 5)
