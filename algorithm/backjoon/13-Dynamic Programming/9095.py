def solution(m):
    d = [0, 1, 2, 4]

    for i in range(4, m+1):
        d.append(0)
        d[i] = d[i-3]+d[i-2]+d[i-1]

    print(d)

solution(4)
solution(7)
solution(10)

d= []

def bt(a):
    if d[a] > 0:
        return d[a]

    d[a] = bt(a-1) + bt(a-2) + bt(a-3)

    return d[a]


def solution(m):
    global d
    d = [0 for x in range(12)]

    d[1] = 1
    d[2] = 2
    d[3] = 4
    bt(m)

    print(d)


solution(4)
solution(7)
solution(10)




def solution(n):
    d = [0 for x in range(n+1)]

    d[1] = 1
    d[2] = 2
    d[3] = 4

    for i in range(4, n+1):
        d[i] = d[i-3] + d[i-2] + d[i-1]

    print(d[n], d)


solution(3)
solution(4)
solution(7)
solution(10)
