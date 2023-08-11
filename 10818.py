# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/10818

import sys
input = sys.stdin.readline

N = int(input())
Num = list(map(int, input().split()))
print(min(Num))
print(max(Num))