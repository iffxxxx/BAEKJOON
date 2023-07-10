# https://www.acmicpc.net/problem/10026

import sys
from collections import deque
sys.setrecursionlimit(1000000) # DFS 사용시 재귀호출 수 제한
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
N = int(input())
Mat = [(list(input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def BFS(y, x):
    queue = deque([(y, x)])
    visited[y][x] = True
    while queue:
        vy, vx = queue.popleft()
        for i in range(4):
            cy = vy + dy[i]
            cx = vx + dx[i]
            if 0 <= cy < N and 0 <= cx < N and Mat[cy][cx] == Mat[y][x] and visited[cy][cx] == False:
                queue.append((cy, cx))
                visited[cy][cx] = True

cnt1, cnt2 = 0, 0

for c in range(N):
    for r in range(N):
        if not visited[c][r]:
            BFS(c, r)
            cnt1 += 1

visited = [[False] * N for _ in range(N)]

for c in range(N):
    for r in range(N):
        if Mat[c][r] == 'R':
            Mat[c][r] = 'G'

for c in range(N):
    for r in range(N):
        if not visited[c][r]:
            BFS(c, r)
            cnt2 += 1

print(cnt1, cnt2)



# 실패한 케이스1 - 시간 초과
# def BFS(y, x, C, RG):
#     queue = deque([(y, x)])
    
#     while queue:
#         vy, vx = queue.popleft()
#         if RG == True:
#             Mat[vy][vx] = C.upper()
#         else:
#             Mat[vy][vx] = C.lower()
#             if Mat[vy][vx] == 'r':
#                 Mat[vy][vx] = 'g'
#         for i in range(4):
#             cy = vy + dy[i]
#             cx = vx + dx[i]
#             if 0 <= cy < N and 0 <= cx < N and Mat[cy][cx] == C:
#                 queue.append((cy, cx))

# cnt1, cnt2 = 0, 0

# for c in range(N):
#     for r in range(N):
#         if Mat[c][r].isupper():
#             BFS(c, r, Mat[c][r], False)
#             cnt1 += 1

# for c in range(N):
#     for r in range(N):
#         if Mat[c][r].islower():
#             BFS(c, r, Mat[c][r], True)
#             cnt2 += 1

# print(cnt1, cnt2)

# 반례
# 5
# RRRRR
# RBBBR
# RBGBR
# RBBBR
# RRRRR


# 실패한 케이스 2 - 시간 초과 in을 사용할 경우 O(N) 의 시간 복잡도
# visited = set()
# def BFS(y, x):
#     visited.add((y, x))
#     queue = deque([(y, x)])
#     while queue:
#         vy, vx = queue.popleft()
#         visited.add((vy, vx))
#         for i in range(4):
#             cy = vy + dy[i]
#             cx = vx + dx[i]
#             if 0 <= cy < N and 0 <= cx < N and Mat[cy][cx] == Mat[y][x] and (cy, cx) not in visited:
#                 queue.append((cy, cx))
                
# cnt1, cnt2 = 0, 0

# for c in range(N):
#     for r in range(N):
#         if (c, r) not in visited:
#             BFS(c, r)
#             cnt1 += 1

# visited = set()
# for c in range(N):
#     for r in range(N):
#         if Mat[c][r] == 'R':
#             Mat[c][r] = 'G'

# for c in range(N):
#     for r in range(N):
#         if (c, r) not in visited:
#             BFS(c, r)
#             cnt2 += 1

# print(cnt1, cnt2)