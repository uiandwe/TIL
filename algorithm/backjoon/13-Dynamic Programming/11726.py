
def solution(n):
    d = [0 for x in range(n+1)]
    d[0] = d[1] = 1
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]

    print(d)


solution(2)
solution(3)
solution(4)
solution(5)
solution(6)
solution(7)
solution(8)
solution(9)
