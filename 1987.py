# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1987

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def BFS():
    global ans
    queue = set([(0, 0, Mat[0][0])])

    while queue:
        y, x, z = queue.pop()
        ans = max(ans, len(z))
        
        for i in range(4):
            cy = y + dy[i]
            cx = x + dx[i]
            if 0 <= cy < N and 0 <= cx < M and Mat[cy][cx] not in z: # visited[ord(Mat[cy][cx]) - 65] == 0:
                queue.add((cy, cx, Mat[cy][cx] + z))
                
# 시간초과 - why?
def DFS(y, x, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        cy = y + dy[i]
        cx = x + dx[i]
        if 0 <= cy < N and 0 <= cx < M and Mat[cy][cx] not in visited: # visited[ord(Mat[cy][cx]) - 65] == 0:
            visited.add(Mat[cy][cx])
            # visited[ord(Mat[cy][cx]) - 65] = 1
            DFS(cy, cx, cnt + 1)
            visited.remove(Mat[cy][cx])
            # visited[ord(Mat[cy][cx]) - 65] = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
N, M = map(int, input().split())
Mat = [list(map(str, input().strip())) for _ in range(N)]

ans = 0
visited = set()
# visited = [0] * 26 # 알파벳 개수 세기

visited.add(Mat[0][0])
# visited[ord(Mat[0][0]) - 65] = 1

DFS(0, 0, 1)
print(ans)

ans = 0
BFS()
print(ans)