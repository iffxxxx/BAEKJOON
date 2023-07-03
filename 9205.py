# https://www.acmicpc.net/problem/9205

import sys
from collections import deque

def BFS(node):
    queue = deque([node[0]])
    visited = set()

    while queue:
        vx, vy = queue.popleft()
        if abs(vx - node[-1][0]) + abs(vy - node[-1][1]) <= 1000:
            print("happy")
            return
        for x, y in node[1 : -1]:
            if (x, y) not in visited:
                if abs(vx - x) + abs(vy - y) <= 1000:
                    visited.add((x, y))
                    queue.append((x, y))
    print("sad")
    return

t = int(sys.stdin.readline())
for i in range(t):
    node = []
    for n in range(int(sys.stdin.readline()) + 2):
        node.append(tuple(map(int, sys.stdin.readline().split())))
    BFS(node)
