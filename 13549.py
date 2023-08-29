# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/13549

import sys
from collections import deque
input = sys.stdin.readline

visited = [-1 for _ in range(100001)]
start, end = map(int, input().split())

queue = deque([start])
visited[start] = 0

while queue:
    p = queue.popleft()
    
    if p == end:
        print(visited[end])
        break
    
    if 0 <= 2 * p <= 100000 and visited[2 * p] == -1:
        visited[2 * p] = visited[p]
        queue.appendleft(2 * p)
        
    if 0 <= p - 1 <= 100000 and visited[p - 1] == -1:
        visited[p - 1] = visited[p] + 1
        queue.append(p - 1)
        
    if 0 <= p + 1 <= 100000 and visited[p + 1] == -1:
        visited[p + 1] = visited[p] + 1
        queue.append(p + 1)