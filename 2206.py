# https://www.acmicpc.net/problem/2206 벽 부수고 이동하기

import sys
from collections import deque

input = sys.stdin.readline
N, M = list(map(int, input().split()))
Mat = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
# visited = [[[0, 0]] * M for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def BFS():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    
    while queue:
        vy, vx, cnt = queue.popleft()
        
        if vy == N - 1 and vx == M - 1:
            return visited[vy][vx][cnt]
        
        for i in range(4):
            cy = vy + dy[i]
            cx = vx + dx[i]
            if 0 <= cy < N and 0 <= cx < M:
                if Mat[cy][cx] == 1 and cnt == 0:
                    visited[cy][cx][cnt + 1] = visited[vy][vx][cnt] + 1
                    queue.append((cy, cx, cnt + 1))
                elif Mat[cy][cx] == 0 and visited[cy][cx][cnt] == 0:
                    visited[cy][cx][cnt] = visited[vy][vx][cnt] + 1
                    queue.append((cy, cx, cnt))
    return -1

print(BFS())