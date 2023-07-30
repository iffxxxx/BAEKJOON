# https://www.acmicpc.net/problem/15655

import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
Num = sorted(list(map(int, input().split())))

stack = []
def BACK(start):
    if len(stack) == M:
        print(*stack)
        return
    for i in range(start, N):
        stack.append(Num[i])
        BACK(i + 1)
        stack.pop()

BACK(0)