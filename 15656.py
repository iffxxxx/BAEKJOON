# https://www.acmicpc.net/problem/15656

import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
Num = sorted(list(map(int, input().split())))

stack = []
def BACK():
    if len(stack) == M:
        print(*stack)
        return
    for i in range(N):
        stack.append(Num[i])
        BACK()
        stack.pop()

BACK()