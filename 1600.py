# https://www.acmicpc.net/problem/1600

import sys
from collections import deque
input = sys.stdin.readline

Mat = []

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
hy = [-1, -2, -2, -1, 1, 2, 2, 1]
hx = [-2, -1, 1, 2, 2, 1, -1, -2]

K = int(input())
W, H = list(map(int, input().split()))
visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]

for _ in range(H):
    Mat.append(list(map(int, input().split())))

def BFS(y, x, cnt):
    queue = deque([(y, x, cnt)])
    visited[y][x][cnt] = 1
    
    while queue:
        vy, vx, cnt = queue.popleft()
        
        if vy == H - 1 and vx == W - 1:
            return visited[vy][vx][cnt] - 1
        
        for i in range(4):
            cy = vy + dy[i]
            cx = vx + dx[i]
            if 0 <= cy < H and 0 <= cx < W and Mat[cy][cx] == 0 and visited[cy][cx][cnt] == 0:
                visited[cy][cx][cnt] = visited[vy][vx][cnt] + 1
                queue.append((cy, cx, cnt))
        
        for j in range(8):
            cy = vy + hy[j]
            cx = vx + hx[j]
            if 0 <= cy < H and 0 <= cx < W and Mat[cy][cx] == 0 and cnt + 1 <= K and visited[cy][cx][cnt + 1] == 0:
                visited[cy][cx][cnt + 1] = visited[vy][vx][cnt] + 1
                queue.append((cy, cx, cnt + 1))

    return -1

print(BFS(0, 0, 0))