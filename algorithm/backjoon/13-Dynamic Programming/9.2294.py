# -*- coding: utf8 -*-

'''
* 몇번째 이상 암될 경우는 그 전 / 그 전전의 값을 비교 해야 한다.
이번 문제는 3개 이상 연속이 안되므로 현재, 현재-1의 값을 가져오며
현재값 a[i], 연속한 값 d[i-1]+a[i], 건너뛴값 d[i-3]+a[i-1]+a[i]
중 최대값을 더해 나가는 식으로 값을 구한다

'''

d = [0]

a = [0, 6, 10, 13, 9, 8, 1]

d.append(a[1])  #0번째 셋팅
d.append(d[1]+ a[2]) #1번째 셋팅

for i in range(3, len(a)):
    d.append(max(d[i-3]+a[i-1]+a[i], d[i-2]+a[i], d[i-1]))



print d
