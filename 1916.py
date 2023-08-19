# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1916

import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijstra(start):
    distance = [INF] * (N + 1)
    queue = []
    
    heapq.heappush(queue, [0, start])
    distance[start] = 0
    
    while queue:
        now_cost, now_vertex = heapq.heappop(queue)
        
        # 기존 최단거리보다 멀다면 무시
        if distance[now_vertex] < now_cost:
            continue
        
        for next_cost, next_vertex in graph[now_vertex]:
            next_cost += now_cost
            if next_cost < distance[next_vertex]:
                distance[next_vertex] = next_cost
                heapq.heappush(queue, [next_cost, next_vertex])
    return distance

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])

start, end = map(int, input().split())

answer = dijstra(start)

print(answer[end])
