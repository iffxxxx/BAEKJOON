# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1715

import sys
import heapq
input = sys.stdin.readline

Num = []
N = int(input())
for _ in range(N):
    heapq.heappush(Num, int(input()))
    
if N == 1:
    print(0)
else:
    answer = 0
    while len(Num) > 1:
        temp1 = heapq.heappop(Num)
        temp2 = heapq.heappop(Num)
        Sum = temp1 + temp2
        answer += Sum
        heapq.heappush(Num, Sum)
    print(answer)

# 실패한 케이스 - 반례 1 1 1 1
# Num = []
# N = int(input())
# for _ in range(N):
#     Num.append(int(input()))

# Num.sort()

# for i in range(1, N):
#     Num[i] += Num[i - 1]

# if N == 1:
#     print(0)
# elif N == 2:
#     print(Num[-1])
# else:
#     print(sum(Num) - Num[0])