# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2562

import sys
input = sys.stdin.readline

Num = [0]
for _ in range(9):
    Num.append(int(input()))

a = max(Num)
print(a)
print(Num.index(a))