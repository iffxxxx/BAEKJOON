# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/10986

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Num = list(map(int, input().split()))
cnt = [0] * M

sum = 0
for i in range(0, N):
    sum += Num[i]
    cnt[sum % M] += 1

answer = cnt[0]
for i in range(M):
    answer += (cnt[i] * (cnt[i] - 1) // 2)

print(answer)