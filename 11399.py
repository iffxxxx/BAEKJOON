# -*- coding: utf-8 -*-
# acmicpc.net/problem/11399

import sys
input = sys.stdin.readline

n = int(input())
Num = sorted(list(map(int, input().split())))

temp = 0
for i in range(n):
    temp += Num[i]
    Num[i] = temp

print(sum(Num))