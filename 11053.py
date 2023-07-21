# https://www.acmicpc.net/problem/11053 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

N = int(input())
Num = list(map(int, input().split()))

Score = [1] * N

for i in range(N):
    for j in range(i):
        if Num[i] > Num[j]:
            Score[i] = max(Score[i], Score[j] + 1)

print(max(Score))