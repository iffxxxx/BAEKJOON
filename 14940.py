# https://www.acmicpc.net/problem/14940

import sys
from collections import deque

mat = []
panel = [[-1, 0], [1, 0], [0, -1], [0, 1]]
n, m = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))

for y in range(n):
    for x in range(m):
        if mat[y][x] == 2:
            mat[y][x] = 0
            start = (y, x)

visited = set((start))

queue = deque([start])
while queue:
    vy, vx = queue.popleft()
    for i in range(4):
        y = vy + panel[i][0]
        x = vx + panel[i][1]
        if 0 <= y < n and 0 <= x < m and (y, x) not in visited and mat[y][x] == 1:
            visited.add((y, x))
            queue.append((y, x))
            mat[y][x] = mat[vy][vx] + 1

for y in range(n):
    for x in range(m):
        if (y, x) not in visited and mat[y][x] == 1:
            mat[y][x] = -1

for i in mat:
    print(*i)