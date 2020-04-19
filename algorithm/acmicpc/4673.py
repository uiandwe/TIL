def self_number(i):
    res = i
    if i >= 10000:
        res += i // 10000
        i %= 10000

    if i >= 1000:
        res += i // 1000
        i %= 1000

    if i >= 100:
        res += i // 100
        i %= 100

    if i >= 10:
        res += i // 10
        i %= 10

    res += i

    return int(res)


def solution():
    max_n = 101
    d = [0 for x in range(max_n)]

    for i in range(1, max_n):
        n = self_number(i)
        if n < max_n-1:
            d[n] = 1

    for i in range(1, max_n):
        if d[i] == 0:
            print(i)

solution()