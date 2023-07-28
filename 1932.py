# https://www.acmicpc.net/problem/1932

import sys
input = sys.stdin.readline

N = int(input())
Num = [list(map(int, input().split())) for _ in range(N)]

for i in range(N - 1):
    for j in range(i + 1):
        if j == 0:
            Num[i + 1][j] += Num[i][0]
        if 0 < j <= i:
            Num[i + 1][j] += max(Num[i][j - 1], Num[i][j])
        if j == 0 or j == i:
            Num[i + 1][-1] += Num[i][-1]

print(max(Num[-1]))

# for i in Num:
#     print(i)