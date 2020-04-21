# -*- coding: utf-8 -*-
def solution(k, t):
    answer = 0

    dp = [[0 for _ in range(k+1)] for _ in range(101)]
    dp[0][t[0][0]] = t[0][1]
    dp[0][t[0][2]] = t[0][3]

    for i in range(1, len(t)): # 도시
        for j in range(k): # 시간
            if dp[i-1][j] == 0:
                continue
            if j + t[i][0] <= k:
                dp[i][j+t[i][0]] = max(dp[i][j+t[i][0]], dp[i-1][j]+t[i][1])
                answer = max(answer, dp[i][j+t[i][0]])

            if j + t[i][2] <= k:
                dp[i][j+t[i][2]] = max(dp[i][j+t[i][2]], dp[i-1][j]+t[i][3])
                answer = max(answer, dp[i][j+t[i][2]])

    return answer



print(solution(1650, [[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]))
