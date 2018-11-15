d = [1, 1]


def fibo(i):
    if i == 0 or i == 1:
        return 1
    if d[i] != 0:
        return d[i]
    else:
        d[i] = d[i - 1] + d[i - 2]
        return d[i]


def solution(n):
    global d
    for i in range(n):
        d.append(0)
        fibo(i)
    print(d)

solution(10)
