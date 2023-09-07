# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/13458

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = N
for a in A:
    a -= B
    if a > 0:
        if a % C == 0:
            answer += a // C
        else:
            answer += a // C + 1
            
print(answer)