# https://www.acmicpc.net/problem/2609

import sys

A, B = map(int, sys.stdin.readline().split())
Aprior = [i for i in range(1, A + 1) if A % i == 0]
Bprior = [i for i in range(1, B + 1) if B % i == 0]

print(x := max(set(Aprior) & set(Bprior)))
print(int(A * B / x))