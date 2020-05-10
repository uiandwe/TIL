# -*- coding: utf-8 -*-
n, m = 5, 5
d = [1, 2, 3, 2, 5]

result = 0
summary = 0
end = 0

for start in range(n):
    while summary < m and end < n:
        summary += d[end]
        end += 1
    if summary == m:
        result += 1
        print((start, end-1, d[start:end]))

    summary -= d[start]

print(result)
