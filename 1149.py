# https://www.acmicpc.net/problem/1149 RGB°Å¸®

import sys
input = sys.stdin.readline

N = int(input())

HOUSE = []
for _ in range(N):
    HOUSE.append(list(map(int, input().split())))

for i in range(N - 1):
    HOUSE[i + 1][0] = min(HOUSE[i][1], HOUSE[i][2]) + HOUSE[i + 1][0]
    HOUSE[i + 1][1] = min(HOUSE[i][0], HOUSE[i][2]) + HOUSE[i + 1][1]
    HOUSE[i + 1][2] = min(HOUSE[i][0], HOUSE[i][1]) + HOUSE[i + 1][2]

print(min(HOUSE[N - 1]))