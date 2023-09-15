# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2475

Num = list(map(int, input().split()))

temp = 0
for i in range(5):
    temp += Num[i] ** 2

print(temp % 10)