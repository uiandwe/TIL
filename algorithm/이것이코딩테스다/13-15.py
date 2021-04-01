# -*- coding: utf-8 -*-
n, m, k, x = list(map(int, input().split()))
print(n, m, k, x)
d = [[0]* (n+1) for _ in range(n+1)]
for i in range(m):
    y, x = list(map(int, input().split()))
    d[y][x] = 1

for a in d:
    print(a)

result = []
visit = [float('inf')] * (n+1)
from collections import deque
q = deque()
q.append((1, 0))

def bfs():
    while q:
        node, depth = q.popleft()
        if depth < visit[node]:
            visit[node] = depth

        for i in range(1, n+1):
            if d[node][i]:
                q.append((i, depth+1))

bfs()
print(visit)


"""
4 4 2 1
1 2
1 3
2 3
2 4
>> 4


4 3 2 1
1 2
1 3
1 4
>> -1


4 4 1 1
1 2
1 3
2 3
2 4
>> 2 3
"""
