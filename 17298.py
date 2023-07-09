# https://www.acmicpc.net/problem/17298

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
Num = list(map(int, input().split()))

stack = deque()     # stack = [] 사용시 1296ms , deque() 사용시 1208ms
answer = [-1] * N

for i in range(N):
    n = Num[i]
    while stack and Num[stack[-1]] < n:
        idx = stack.pop()
        answer[idx] = n
    stack.append(i)

print(*answer)