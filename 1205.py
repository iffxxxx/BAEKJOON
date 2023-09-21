# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1205

import sys
input = sys.stdin.readline

n, m, p = map(int, input().split())
Num = list(map(int, input().split())) + [m]
Num.sort(reverse= True)
idx = Num.index(m) + 1

if n:
    if idx > p:
        print(-1)
    else:
        if n == p and m == Num[-1]:
            print(-1)
        else:
            print(idx)
else:
    print(1)