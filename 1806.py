# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1806 ºÎºÐÇÕ

import sys
input = sys.stdin.readline

N, S = list(map(int, input().split()))
Num = [0] + list(map(int, input().split()))

for i in range(1, N + 1):
    Num[i] = Num[i - 1] + Num[i]

start, end = 0, 1
length = 100001     # sys.maxsize
while start < end <= N:
    if Num[end] - Num[start] >= S:
        length = min(length, end - start)
        start += 1
    elif Num[end] - Num[start] < S:
        end += 1
    

if length == 100001:
    print(0)
else:
    print(length)