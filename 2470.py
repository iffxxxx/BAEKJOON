# https://www.acmicpc.net/problem/2470 두 용액

import sys
input = sys.stdin.readline

# 입력
N = int(input())
Num = sorted(list(map(int, input().split())))

# 투포인터
B = sys.maxsize
L, R = 0, N - 1
answer = []

while L < R:
    A = Num[L] + Num[R]
    if abs(A) < B:
        B = abs(A)
        answer = [Num[L], Num[R]]
    if A == 0:
        break
    elif A > 0:
        R -= 1
    elif A < 0:
        L += 1

print(*answer)