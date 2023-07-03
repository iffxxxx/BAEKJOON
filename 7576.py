# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

start = []
row, col = map(int, input().split())
mat = [list(map(int, input().split())) for i in range(col)]
offset = [[-1, 0], [0, 1], [0, -1], [1, 0]] 

for i in range(col):
    for j in range(row):
        if mat[i][j] == 1:
            start.append((i, j))

queue = deque(start)

while queue:
    vy, vx = queue.popleft()
    for i in range(4):
        y = vy + offset[i][0]
        x = vx + offset[i][1]
        
        if 0 <= y < col and 0 <= x < row and mat[y][x] == 0:
            queue.append((y, x))
            mat[y][x] = mat[vy][vx] + 1

matzero = [i for i in mat if 0 in i]
matmax = [max(i) for i in mat]

if len(matzero) >= 1:
    print(-1)
elif max(matmax) == 1:
    print(0)
else:
    print(max(matmax) - 1)


# 실패한 케이스 1

# import numpy as np

# counter = Counter(np.array(mat).flatten().tolist())
# zero = [0]
# zero.append(counter[0])
# cnt = 1
# while zero[cnt - 1] != zero[cnt]:
#     for c in range(col):
#         for r in range(row):
#             if mat[c][r] == 1:
#                 for i in range(4):
#                     x = r + offset[i][0]
#                     y = c + offset[i][1]
#                     if 0 <= x < row and 0 <= y < col and mat[y][x] == 0:
#                         mat[y][x] += 1
#     counter = Counter(np.array(mat).flatten().tolist())
#     print(mat)
#     zero.append(counter[0])
#     cnt += 1
# print(zero)

# if cnt == 2:
#     print(0)
# elif cnt >= 3:
#     if counter[0] == 0:
#         print(cnt - 2)
#     else:
#         print(-1)