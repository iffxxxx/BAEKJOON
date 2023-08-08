# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/7453

import sys
input = sys.stdin.readline

N = int(input())
Mat = [list(map(int, input().split())) for _ in range(N)]

AB, CD = [], []
for i in range(N):
    for j in range(N):
        AB.append(Mat[i][0] + Mat[j][1])
        CD.append(Mat[i][2] + Mat[j][3])

AB.sort()
CD.sort()

cnt = 0
start, end = 0, len(CD) - 1
while start < len(AB) and end >= 0:
    L, R = AB[start], CD[end]
    if L + R == 0:
        nL, nR = start + 1, end - 1
        while nL < len(AB) and AB[nL] == AB[start]:
            nL += 1
        while nR >= 0 and CD[nR] == CD[end]:
            nR -= 1
        cnt += (start - nL) * (nR - end)
        start, end = nL, nR
    elif L + R > 0:
        end -= 1
    else:
        start += 1

print(cnt)


# 실패한 케이스 - 시간초과 아마 in?
# AB, CD = {}, {}
# for i in range(N):
#     for j in range(N):
#         ab = Mat[i][0] + Mat[j][1]
#         if ab not in AB.keys():
#             AB[ab] = 1
#         else:
#             AB[ab] += 1
#         cd = Mat[i][2] + Mat[j][3]
#         if cd not in CD.keys():
#             CD[cd] = 1
#         else:
#             CD[cd] += 1
            
# left = sorted(AB.keys())
# right = sorted(CD.keys())

# cnt = 0
# start, end = 0, len(right) - 1
# while start < len(left) and end >= 0:
#     L, R = left[start], right[end]
#     if L + R == 0:
#         cnt += AB[L] * CD[R]
#         start += 1
#         end -= 1
#     elif L + R > 0:
#         end -= 1
#     else:
#         start += 1

# print(cnt)