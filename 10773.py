# https://www.acmicpc.net/problem/10773

import sys

K = int(input())
num = []
for _ in range(K):
    num.append(int(sys.stdin.readline()))
    
stack = []
for i in num:
    if i == 0:
        stack.pop()
    else:
        stack.append(i)
print(sum(stack))