# https://www.acmicpc.net/problem/2667

import sys
from collections import deque

N = int(sys.stdin.readline())

# DFS
mat = []
answer = []
cnt = 0

for _ in range(N):
    mat.append(list(map(int, sys.stdin.readline().strip())))

y_panel = [-1, 1, 0, 0]
x_panel = [0, 0, -1, 1]

def DFS(y, x):
    global cnt
    
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    
    if mat[y][x] == 1:
        cnt += 1
        mat[y][x] = 0
        for i in range(4):
            ny = y + y_panel[i]
            nx = x + x_panel[i]
            DFS(ny, nx)

for y in range(N):
    for x in range(N):
        if mat[y][x] == 1:
            DFS(y, x)
            answer.append(cnt)
            cnt = 0

print(len(answer))
for i in sorted(answer):
    print(i)


# BFS - ¼º°ø
# def BFS(mat, a, b):
#     queue = deque([(a, b)])
#     cnt = 1
#     while queue:
#         vy, vx = queue.popleft()
#         for i in range(4):
#             y = vy + y_panel[i]
#             x = vx + x_panel[i]
#             if 0 <= y < N and 0 <= x < N and mat[y][x] == 1:
#                 cnt += 1
#                 mat[y][x] = 0
#                 queue.append((y, x))
#     return cnt
                    
# answer = []
# for y in range(N):
#     for x in range(N):
#         if mat[y][x] == 1:
#             mat[y][x] = 0
#             answer.append(BFS(mat, y, x))

# print(len(answer))
# for i in sorted(answer):
#     print(i)