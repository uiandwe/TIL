def solution(p, c):
    d = {}
    for name in p:
        if name in d:
            d[name] += 1
        else:
            d[name] = 1

    for name in c:
        if name in d:
            d[name] -= 1

    for name in d:
        if d[name] == 1:
            return name
