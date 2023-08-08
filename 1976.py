# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1976

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())
# 부모테이블 생성
parent = [i for i in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            union(i, j)

parent = [-1] + parent
Plan = list(map(int, input().split()))
start = parent[Plan[0]]

for i in range(1, M):
    if parent[Plan[i]] != start:
        print("NO")
        break
else:
    print("YES")
