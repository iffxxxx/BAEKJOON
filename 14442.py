# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/14442

import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
Mat = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def BFS(sy, sx, c):
    queue = deque([(sy, sx, c)])
    visited[sy][sx][c] = 1
    while queue:
        vy, vx, cnt = queue.popleft()
        if vy == N - 1 and vx == M - 1:
            return visited[vy][vx][cnt]
        
        for i in range(4):
            y = vy + dy[i]
            x = vx + dx[i]
            if 0 <= y < N and 0 <= x < M:
                if Mat[y][x] == 0 and visited[y][x][cnt] == 0:
                    queue.append((y, x, cnt))
                    visited[y][x][cnt] = visited[vy][vx][cnt] + 1
                elif Mat[y][x] == 1 and cnt < K and visited[y][x][cnt + 1] == 0:
                    queue.append((y, x, cnt + 1))
                    visited[y][x][cnt + 1] = visited[vy][vx][cnt] + 1
    return -1

print(BFS(0, 0, 0))