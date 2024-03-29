# -*- coding: utf-8 -*-
"""
피보나치 배열은 0과 1로 시작하며, 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다.

정수 N이 주어지면, N보다 작은 모든 짝수 피보나치 수의 합을 구하여라.


Fibonacci sequence starts with 0 and 1 where each fibonacci number

is a sum of two previous fibonacci numbers. Given an integer N,

find the sum of all even fibonacci numbers.


예제)

Input: N = 12

Output: 10 // 0, 1, 2, 3, 5, 8 중 짝수인 2 + 8 = 10.


"""

from functools import lru_cache

@lru_cache()
def fibo(n):
    if n <= 2:
        return n


    return fibo(n-2) + fibo(n-1)

def solution(N):
    ret_value = 0
    for i in range(N+1):

        temp = fibo(i)

        if temp >= N:
            break

        if fibo(i) % 2 == 0:
            ret_value += temp
    
    return ret_value


assert solution(12) == 10
