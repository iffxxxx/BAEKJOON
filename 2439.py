# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2439

import sys
input = sys.stdin.readline

N = int(input())
for i in range(1, N + 1):
    print(" " * (N - i), end = "")
    print('*' * i)