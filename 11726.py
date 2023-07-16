# https://www.acmicpc.net/problem/11726 2*n ≈∏¿œ∏µ

import sys
N = int(sys.stdin.readline())
Num = [1, 1]
for i in range(1, N):
    Num.append(Num[i] + Num[i - 1])
print(Num[N] % 10007)