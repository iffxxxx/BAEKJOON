# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1271

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
print(N // M)
print(N % M)