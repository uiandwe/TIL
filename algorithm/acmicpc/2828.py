# -*- coding: utf-8 -*-
n, m = map(int, input().split(" "))

j = int(input())

start = 1
end = start + (m-1)

answer = 0
for i in range(j):
    apple = int(input())
    if start <= apple <= end:
          continue
    else:
        p1 = abs(apple-start)
        p2 = abs(apple-end)

        if p1 <= p2:
            answer += p1
            start = apple
            end = start + (m-1)
        else:
            answer += p2
            end = apple
            start = apple - (m-1)

print(answer)
