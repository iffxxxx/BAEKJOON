# https://www.acmicpc.net/problem/11053 ���� �� �����ϴ� �κ� ����

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