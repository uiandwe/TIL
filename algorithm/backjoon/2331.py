import math

A = input()
P = input()

check = [A]

v = A
for i in range(20):
    c = 0
    for temp in str(v):
        c += int(math.pow(int(temp), P))
    v = c

    if v in check:
        check = check[0:check.index(v)]
        break
    else:
        check.append(c)


print check
