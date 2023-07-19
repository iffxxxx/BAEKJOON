# https://www.acmicpc.net/problem/15654 N°ú M (5)

import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
Num = list(map(int, input().split()))
Num.sort()

stack = []
def BACK():
    if len(stack) == M:
        print(*stack)
        return
    for i in range(N):
        if Num[i] not in stack:
            stack.append(Num[i])
            BACK()
            stack.pop()

BACK()