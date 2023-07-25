# https://www.acmicpc.net/problem/14503

import sys
input = sys.stdin.readline

Mat = []
Dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
N, M = list(map(int, input().split()))
y, x, d = list(map(int, input().split()))
for _ in range(N):
    Mat.append(list(map(int, input().split())))

while True:
    Mat[y][x] = 2
    cnt = 0
    for i in range(4):
        ny = y + Dir[i][0]
        nx = x + Dir[i][1]
        if Mat[ny][nx] == 1 or Mat[ny][nx] == 2:
            cnt += 1
    if cnt == 4:
        ny = y - Dir[d][0]
        nx = x - Dir[d][1]
        if Mat[ny][nx] == 1:
            break
        elif Mat[ny][nx] == 2:
            y = ny
            x = nx
    else:
        for _ in range(4):
            d = (d + 3) % 4
            ny = y + Dir[d][0]
            nx = x + Dir[d][1]
            if Mat[ny][nx] == 0:
                y = ny
                x = nx
                break

Sum = 0
for mat in Mat:
    Sum += mat.count(2)

print(Sum)