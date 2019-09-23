# -*- coding: utf-8 -*-
def knapsack(W, wt, val, n):  # W: 배낭의 무게한도, wt: 각 보석의 무게, val: 각 보석의 가격, n: 보석의 수
    K = [[0 for x in range(W+1)] for x in range(n+1)]  # DP를 위한 2차원 리스트 초기화
    for i in range(n+1):
        for w in range(W+1):  # 각 칸을 돌면서
            K[i][w] = K[i - 1][w]
            if wt[i-1] <= w:  # 점화식을 그대로 프로그램으로
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])  # max 함수 사용하여 큰 것 선택

    return K[n][W]



print(knapsack(12, [3, 4, 5], [6, 3, 5], 3))


def solution(n):
    size = [3, 4, 5]
    value = [6, 3, 5]

    d = [[0 for i in range(n+2)] for j in range(len(size)+1)]

    for i in range(len(size)):
        for j in range(n+1):
            if size[i] <= j:
                d[i][j] = d[i-1][j]
                d[i][j] = max(value[i] + d[i-1][j-size[i]], d[i][j])

    return d[len(size)-1][n]



print(solution(12))
