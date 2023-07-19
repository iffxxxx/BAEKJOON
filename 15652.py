# https://www.acmicpc.net/problem/15652 N°ú M (4)

import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

stack = []
def BACK(start):
    if len(stack) == M:
        print(*stack)
        return
    
    for i in range(start, N + 1):
        stack.append(i)
        BACK(i)
        stack.pop()

BACK(1)