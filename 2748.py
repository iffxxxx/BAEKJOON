# https://www.acmicpc.net/problem/2748 �Ǻ���ġ �� 2

import sys
N = int(sys.stdin.readline())
Num = [0, 1]
for i in range(0, N - 1):
    Num.append(Num[i] + Num[i + 1])
print(Num[N])