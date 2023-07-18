# https://www.acmicpc.net/problem/15651 - N°ú M (3)

import sys
N, M = list(map(int, sys.stdin.readline().split()))

stack = []
def BACK():
    if len(stack) == M:
        print(*stack)
        return
    
    for i in range(1, N + 1):
        stack.append(i)
        BACK()
        stack.pop()

BACK()