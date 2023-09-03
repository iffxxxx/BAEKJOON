# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1874

import sys
input = sys.stdin.readline

N = int(input())
Num = []
for _ in range(N):
    Num.append(int(input()))

cnt = 0
stack = []
answer = []
for i in range(1, N + 1):
    stack.append(i)
    answer.append('+')
    
    while stack and stack[-1] == Num[cnt]:
        cnt += 1
        stack.pop()
        answer.append('-')

if len(stack) == 0:
    for i in answer:
        print(i)
else:
    print("NO")