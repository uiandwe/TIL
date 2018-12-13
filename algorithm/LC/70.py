def solution(state):
    d = [0 for x in range(state+1)]
    d[0] = 1
    d[1] = 1
    d[2] = 2
    if state == 1:
        return d[1]

    for i in range(2, state+1):
        d[i] = d[i-1] + d[i-2]
    print(d)
    return d[state]


print(solution(2))
print(solution(3))
print(solution(10))
