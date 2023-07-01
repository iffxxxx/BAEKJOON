# https://www.acmicpc.net/problem/11659

import sys

N, M = map(int, sys.stdin.readline().split())
num = [0] + list(map(int, sys.stdin.readline().split()))
cnt = 0
for i, n in enumerate(num):
    cnt += n
    num[i] = cnt

index = []
for _ in range(M):
    index.append(list(map(int, sys.stdin.readline().split())))
    
for s, e in index:
    print(num[e] - num[s - 1])


# 실패한 케이스 1 - 시간초과
# for s, e in index:
#     print(sum(num[s - 1: e]))