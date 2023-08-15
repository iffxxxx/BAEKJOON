# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1753

import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijstra(start):
    distance = [INF] * (V + 1)
    queue = []
    
    heapq.heappush(queue, [0, start])   # 큐에 [거리, 노드]로 우선순위 지정
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

start = int(input())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])

answer = dijstra(start)

for i in range(1, V + 1):
    if answer[i] == INF:
        print("INF")
    else:
        print(answer[i])