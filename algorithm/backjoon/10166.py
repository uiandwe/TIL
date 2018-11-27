def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a


def solution(a, b):
    d = []
    total = 0
    for i in range(b+1):
        temp = []
        for j in range(b+1):
            temp.append(0)
        d.append(temp)

    for i in range(a, b+1):
        for j in range(1, i+1):
            g = gcd(j, i)
            tempj = int(j/g)
            tempi = int(i/g)

            if d[tempi][tempj] != 1:
                d[tempi][tempj] = 1
                total += 1

    print(total)

solution(3, 6)
