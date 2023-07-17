# https://www.acmicpc.net/problem/1463 1로 만들기

import sys
N = int(sys.stdin.readline())

Num = [0] * (N + 1)

for i in range(2, N + 1):
    Num[i] = Num[i - 1] + 1
    if i % 2 == 0:
        Num[i] = min(Num[i], Num[i // 2] + 1)
    if i % 3 == 0:
        Num[i] = min(Num[i], Num[i // 3] + 1)

print(Num[N])