# -*- coding: utf-8 -*-
import heapq

n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [float('inf')]*(n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

dijkstra(start)
print(distance)

"""
3 2 1
1 2 4
1 3 2
[inf, 0, 4, 2]
"""
