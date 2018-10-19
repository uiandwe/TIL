a = []
check = []
for i in range(7+1):
    temp = []

    for j in range(7+1):
        temp.append(0)
    a.append(temp)
    check.append(0)

for i in range(6):
    str = raw_input()
    str = str.split(' ')
    node1 = str[0]
    node2 = str[1]

    a[int(node1)][int(node2)] = 1
    a[int(node2)][int(node1)] = 1


for i in a:
    print i


def dfs(x):
    check[x] = 1
    print x
    for i in range(1, 6+1):
        if a[x][i] == 1 and check[i] == 0:
            dfs(i)


dfs(1)

print check
