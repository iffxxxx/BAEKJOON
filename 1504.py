# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1504

import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijstra(start):
    distance = [INF] * (V + 1)
    queue = []
    
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    
    while queue:
        now_cost, now_vertex = heapq.heappop(queue)
        
        for next_cost, next_vertex in graph[now_vertex]:
            next_cost += now_cost
            if next_cost < distance[next_vertex]:
                distance[next_vertex] = next_cost
                heapq.heappush(queue, [distance[next_vertex], next_vertex])
    return distance

V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])
    graph[v].append([w, u])

v1, v2 = map(int, input().split())
one = dijstra(1)
v1_dis = dijstra(v1)
v2_dis = dijstra(v2)

v1_path = one[v1] + v1_dis[v2] + v2_dis[V]
v2_path = one[v2] + v2_dis[v1] + v1_dis[V]

answer = min(v1_path, v2_path)
if answer >= INF:
    print(-1)
else:
    print(answer)