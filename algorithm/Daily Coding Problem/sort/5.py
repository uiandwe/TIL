# -*- coding: utf-8 -*-
def solution(arr, n):
    arr = sorted(arr, reverse=True)
    print(arr)
    print(arr[n-1])


solution([-1, 3, -1, 5, 4], 2 )

solution([2, 4, -2, -3, 8], 1 )

solution([-5, -3, 1], 3 )
