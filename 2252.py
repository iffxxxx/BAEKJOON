# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2252

import sys
from collections import deque
input = sys.stdin.readline

# 노드의 개수와 간선의 개수를 입력 받기
V, E = map(int, input().split())

# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (V + 1)

# 각 노드에 연결된 간선 정보를 담기 위해 연결 리스트 초기화
graph = [[] for _ in range(V + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)  # 정점 A에서 B로 이동 가능
    indegree[B] += 1    # 진입 차수를 1 증가 why?
    
# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    queue = deque() # 큐 기능을 위한 deque 라이브러리 사용
    
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, V + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소 꺼내기
        now = queue.popleft()
        result.append(now)
        
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                queue.append(i)

    print(*result)

topology_sort()