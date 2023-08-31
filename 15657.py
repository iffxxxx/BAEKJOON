# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/15657

N, M = map(int, input().split())
Num = sorted(list(map(int, input().split())))

stack = []
def BACK(start):
    if len(stack) == M:
        print(*stack)
        return
    for i in range(start, N):
        stack.append(Num[i])
        BACK(i)
        stack.pop()

BACK(0)