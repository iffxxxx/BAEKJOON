# https://www.acmicpc.net/problem/2178

import sys
from collections import deque

# �Է�
maze = []
panel = [[1, 0], [0, 1], [-1, 0], [0, -1]]
N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    maze.append(list(map(int, list(input()))))

def BFS(grafh, start):
    queue = deque([start])
    
    while queue:
        vy, vx = queue.popleft()
        for i in range(4):
            y = vy + panel[i][0]
            x = vx + panel[i][1]
            if 0 <= y < N and 0 <= x < M and maze[y][x] == 1:
                queue.append((y, x))
                maze[y][x] = maze[vy][vx] + 1
    return maze[N - 1][M - 1]

print(BFS(maze, (0, 0)))


# ������ ���̽� 1 - ���� ���ڱ�
# while [x, y] != [N - 1, M - 1]:
#     print(y, x)
#     if maze[y][x] == 1:
#         if x + 1 < M and maze[y][x + 1] == 1:   # ���������� �̵�
#             maze[y][x] = 2
#             x += 1
#         elif y + 1 < N and maze[y + 1][x] == 1: # �Ʒ��� �̵�
#             maze[y][x] = 2
#             y += 1
#         else:
#             if 0 <= y - 1 and maze[y][x - 1] == 1:   # �������� �̵�
#                 maze[y][x] = 2
#                 x -= 1
#             elif 0 <= y - 1 and maze[y - 1][x] == 1:   # ���� �̵�
#                 maze[y][x] = 2
#                 y -= 1


# ������ ���̽� 2
# ��ǥ ���� - �� ��ҿ� �̸� �ٿ��ֱ�
# pos_list = []
# for i in range(N):
#     for j in range(M):
#         pos_list.append([i, j])

# # �׷��� �����
# graph = {}
# for i in range(N * M):
#     vy = pos_list[i][0]
#     vx = pos_list[i][1]
#     if maze[vy][vx] == 1:
#         for dy, dx in panel:
#             y = vy + dy
#             x = vx + dx
#             if 0 <= y < N and 0 <= x < M and maze[y][x] == 1:
#                 j = pos_list.index([y, x])
#                 if i not in graph:
#                     graph[i] = [j]
#                 elif j not in graph[i]:
#                     graph[i] += [j]
                
#                 if j not in graph:
#                     graph[j] = [i]
#                 elif i not in graph[j]:
#                     graph[j] += [i]
# print(graph)

# # �ʺ�켱Ž��
# def BFS(graph, start):
#     visited = []
#     queue = deque([start])
    
#     while queue:
#         v = queue.popleft()
        
#         if v not in visited:
#             visited.append(v)
#             temp = list(set(graph[v]) - set(visited))
#             queue += sorted(temp)
#     return visited
# print(BFS(graph, 0))