# -*- coding: utf-8 -*-
def solution(n):
    if n % 2 != 0:
        return 0

    d = [0, 3, 11]
    if n < 3:
        return d[n]

    for i in range(3, (n//2)+1):
        # f(n) = f(n-2) * 3 + f(n-4) * 2 + f(n-6) * 2 .... + 2
        d.append(d[i-1] * 3 + sum(d[1:i-1])*2 + 2)
    print(d)

    return d[n//2]

solution(4)
solution(6)
solution(8)
