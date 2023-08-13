# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
Mat = []
for _ in range(N):
    Mat.append(list(map(int, input().split())))

H = []
C = []
for i in range(N):
    for j in range(N):
        if Mat[i][j] == 1:
            H.append((i, j))
        elif Mat[i][j] == 2:
            C.append((i, j))

cnt = sys.maxsize
for c in combinations(C, M):
    temp = 0
    for hy, hx in H:
        CD = sys.maxsize
        for cy, cx in c:
            CD = min(CD, abs(hy - cy) + abs(hx - cx))
        temp += CD
    cnt = min(cnt, temp)
print(cnt)