# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2473

import sys
input = sys.stdin.readline

N = int(input())
Num = sorted(list(map(int, input().split())))

Sum = sys.maxsize
answer = []

for i in range(N - 2):
    con = Num[i]
    left, right = i + 1, N - 1
    while left < right:
        cur_sum = Num[left] + Num[right] + con
        if abs(cur_sum) <= Sum:
            answer = [Num[i], Num[left], Num[right]]
            Sum = abs(cur_sum)
        if cur_sum < 0:
            left += 1
        elif cur_sum > 0:
            right -= 1
        else:
            print(*answer)
            sys.exit()

print(*answer)