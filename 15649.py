# https://www.acmicpc.net/problem/15649

import sys

N, M = list(map(int, sys.stdin.readline().split()))

answer = []
def BACK():
    if len(answer) == M:
        print(*answer)
        return
    
    for i in range(1, N + 1):
        if i not in answer:
            answer.append(i)
            BACK()
            answer.pop()

BACK()