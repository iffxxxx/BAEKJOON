# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/2580

import sys
input = sys.stdin.readline

Mat = [list(map(int, input().split())) for _ in range(9)]
Blank = []

for i in range(9):
    for j in range(9):
        if Mat[i][j] == 0:
            Blank.append((i, j))

dy, dx = [0, 1, 2] * 3, [0, 1, 2] * 3

def row_possible(y, s):
    for i in range(9):
        if Mat[y][i] == s:        # 가로
            return False
    return True

def col_possible(x, s):
    for i in range(9):
        if Mat[i][x] == s:        # 세로
            return False
    return True

def sq_possible(y, x, s):       
    ty, tx = y // 3 * 3, x // 3 * 3
    for i in range(3):              # 정사각형
        for j in range(3):
            if Mat[ty + i][tx + j] == s:
                return False
    return True

def BACK(cnt):
    if cnt == len(Blank):
        for i in Mat:
            print(*i)
        exit(0)
    
    y, x = Blank[cnt]
    for i in range(1, 10):
        if row_possible(y, i) and col_possible(x, i) and sq_possible(y, x, i):
            Mat[y][x] = i
            BACK(cnt + 1)
            Mat[y][x] = 0

# BACK(0)



# 실패한 케이스 -> 성공했음

def possible(y, x):
    Num = [i for i in range(1, 10)]
    for i in range(9):
        if Mat[y][i] in Num:        # 가로
            Num.remove(Mat[y][i])
        if Mat[i][x] in Num:        # 세로
            Num.remove(Mat[i][x])
            
    ty, tx = y // 3 * 3, x // 3 * 3
    for i in range(3):              # 정사각형
        for j in range(3):
            if Mat[ty + i][tx + j] in Num:
                Num.remove(Mat[ty + i][tx + j])
    
    return Num

def BACK2(cnt):
    if cnt == len(Blank):
        for i in Mat:
            print(*i)
        exit(0)
    
    y, x = Blank[cnt]
    noc = possible(y, x)
    for i in noc:
        Mat[y][x] = i
        BACK2(cnt + 1)
        Mat[y][x] = 0

BACK2(0)