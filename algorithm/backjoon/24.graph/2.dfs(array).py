a = []
check = []
for i in range(6+1):
    temp = []

    for j in range(6+1):
        temp.append(0)
    a.append(temp)
    check.append(0)

for i in range(7):
    num1 = input()
    num2 = input()

    a[num1][num2] = 1
    a[num2][num1] = 1


for i in a:
    print i



def dfs(x):
    check[x] = 1
    print x
    for i in range(1, 6+1):
        if a[x][i] == 1 and check[i] == 0:
            dfs(i)


dfs(1)
