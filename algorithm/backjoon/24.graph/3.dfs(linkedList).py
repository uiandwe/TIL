a = []
check = []

for i in range(6+1):
    a.append([])
    check.append(0)


for i in range(7*2):
    str = raw_input()
    str = str.split(' ')
    node = str[0]
    v = str[1]
    w = str[2]

    vector = [int(v), int(w)]
    a[int(node)].append(vector)


for i in a:
    print i



def dfs(x):
    check[x] = 1
    print x
    for i in range(len(a[x])):
        y = a[x][i][0]
        if check[y] == 0:
            dfs(y)


dfs(1)
