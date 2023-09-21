# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2577

import sys
input = sys.stdin.readline

temp = 1
for _ in range(3):
    temp *= int(input())

answer = list(str(temp))
for i in range(10):
    print(answer.count(str(i)))