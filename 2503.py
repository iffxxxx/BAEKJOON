# https://www.acmicpc.net/problem/2503 숫자야구

import sys
from itertools import permutations
input = sys.stdin.readline

def ABLE(m, s, b):
    able = []
    s_Num, b_Num = 0, 0
    for i in permutations('123456789', 3):
        s_Num = sum(i[j] ==  m[j] for j in range(3))
        b_Num = sum(i[j] in m for j in range(3))
        if s == s_Num and b == b_Num - s_Num:
            able += [i]
    return able

answer = []
N = int(input())
for _ in range(N):
    M, S, B = list(map(int, input().split()))
    able = ABLE(str(M), S, B)
    if len(answer) == 0:
        answer = able
    else:
        answer = [i for i in able if i in answer]

print(len(answer))