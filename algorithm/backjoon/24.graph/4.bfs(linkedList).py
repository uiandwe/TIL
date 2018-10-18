import queue

a = []
check = []
path = []
q = queue.Queue()


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


q.push(1)
check[1] = 1

while q.empty() is False:
    x = q.front()
    q.pop()
    print x

    for i in range(len(a[x])):
        next = a[x][i][0]
        if check[next] == 0:
            check[next] = 1
            q.push(next)



