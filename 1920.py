# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다.
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다.
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

import sys

n = int(input())
A = list(map(int, (sys.stdin.readline().split())))
A = set(A[:n])
m = int(input())
M = list(map(int, (sys.stdin.readline().split())))
M = M[: m]

for i in M:
    print(1) if i in A else print(0)