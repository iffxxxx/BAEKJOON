# https://www.acmicpc.net/problem/9095 1,2,3 ¥ı«œ±‚

import sys

input = sys.stdin.readline

def FUNC(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x == 3:
        return 4
    else:
        return FUNC(x - 1) + FUNC(x - 2) + FUNC(x - 3)

for _ in range(int(input())):
    print(FUNC(int(input())))