# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/3190

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Mat = [[0] * N for _ in range(N)]
Dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for _ in range(int(input())):
    y, x = map(int, input().split())
    Mat[y - 1][x - 1] = 2

L = int(input())
dir_cnt = 0
dir_list = {}
for _ in range(L):
    c, d = input().split()
    if d == "L":
        dir_cnt = (dir_cnt - 1) % 4
    else:
        dir_cnt = (dir_cnt + 1) % 4
    dir_list[int(c)] = dir_cnt

cnt = 0
turn = 0
y, x = 0, 0
Mat[y][x] = 1
queue = deque([(y, x)])

while True:
    cnt += 1
    y, x = y + Dir[turn][0], x + Dir[turn][1]
    
    if 0 <= y < N and 0 <= x < N:
        if Mat[y][x] == 1:
            break
        elif Mat[y][x] == 0:
            Mat[y][x] = 1
            queue.append((y, x))
            ty, tx = queue.popleft()
            Mat[ty][tx] = 0
        elif Mat[y][x] == 2:
            Mat[y][x] = 1
            queue.append((y, x))
    else:
        break
    
    if cnt in dir_list:
        turn = dir_list[cnt]

print(cnt)