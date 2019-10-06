def solution(N):
    if N == 1:
        return 4
    if N == 2:
        return 6
    if N == 3:
        return 10
    
    d = [0 for x in range(N+1)]
    d[1] = 1
    d[2] = 1
    
    for i in range(2, N+1):
        d[i] = d[i-1]+d[i-2]
    
    return (d[N-1]+d[N])*2 + d[N]*2
    
assert solution(1) == 4
assert solution(2) == 6
assert solution(3) == 10
assert solution(4) == 16
assert solution(5) == 26
assert solution(6) == 42
