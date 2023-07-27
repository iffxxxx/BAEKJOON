# https://www.acmicpc.net/problem/16173

import sys
from collections import deque
input = sys.stdin.readline

Mat = []
dy = [0, 1]
dx = [1, 0]
N = int(input())
for _ in range(N):
    Mat.append(list(map(int, input().split())))
visited = [[0 for _ in range(N)] for _ in range(N)]

def DFS():
    queue = deque([(0, 0)])
    
    while queue:
        vy, vx = queue.popleft()
        visited[vy][vx] = 1
        
        if vy == N - 1 and vx == N - 1:
            return("HaruHaru")
        
        for i in range(2):
            y = vy + dy[i] * Mat[vy][vx]
            x = vx + dx[i] * Mat[vy][vx]
            if 0 <= y < N and 0 <= x < N and visited[y][x] == 0:
                queue.append((y, x))
                visited[y][x] == 1
    return("Hing")

print(DFS())