# https://www.acmicpc.net/problem/15650 - N°ú M (2)

import sys
N, M = list(map(int, sys.stdin.readline().split()))

stack = []
def BACK(start):
    if len(stack) == M:
        print(*stack)
        return

    for i in range(start, N + 1):
        if i not in stack:        
            stack.append(i)
            BACK(i + 1)
            stack.pop()
BACK(1)