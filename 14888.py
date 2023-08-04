# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/14888

import sys
input = sys.stdin.readline

N = int(input())
Num = list(map(int, input().split()))
cnt = list(map(int, input().split()))

Max = -sys.maxsize
Min = sys.maxsize

def BACK(depth, total, plus, minus, multi, divide):
    global Max, Min
    if depth == N:
        Max = max(total, Max)
        Min = min(total, Min)
        return
    
    if plus > 0:
        BACK(depth + 1, total + Num[depth], plus - 1, minus, multi, divide)
    if minus > 0:
        BACK(depth + 1, total - Num[depth], plus, minus - 1, multi, divide)
    if multi > 0:
        BACK(depth + 1, total * Num[depth], plus, minus, multi - 1, divide)
    if divide > 0:
        BACK(depth + 1, int(total / Num[depth]), plus, minus, multi, divide - 1)
        # print(-10 // 3)       -4
        # print(int(-10 / 3))   -3

BACK(1, Num[0], cnt[0], cnt[1], cnt[2], cnt[3])
print(Max)
print(Min)



# 실패한 케이스 - 조건 : 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행
# Num = list(input().rstrip().split())

# Op = ['+', '-', '*', '//']
# Opr = []
# for i in range(4):
#     for j in range(cnt[i]):
#         Opr.append(Op[i])

# stack = []
# permu = []
# def BACK():
#     if len(stack) == N - 1:
#         permu.append(stack[:])
#         return
    
#     for i in range(N - 1):
#         if i not in stack:
#             stack.append(i)
#             BACK()
#             stack.pop()
# BACK()

# answer = []
# for i in range(len(permu)):
#     temp = ''
#     for j in range(N - 1):
#         temp += Num[j] + Opr[permu[i][j]]
#     temp += Num[-1]
#     print(temp)
#     print(eval(temp))
