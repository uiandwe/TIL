num = input()

d = [[0,0,0,0,0,0,0,0,0,0,0],
     [0,1,1,1,1,1,1,1,1,1,0]]

for i in range(2, num+1):
    temp = [0,0,0,0,0,0,0,0,0,0,0]

    d.append(temp)

    for j in range(10):
        if j == 0:
            d[i][j] = d[i-1][j+1]
        elif j == 9:
            d[i][j] = d[i-1][j-1]
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]


print d
print sum(d[num])
