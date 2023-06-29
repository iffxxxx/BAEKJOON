# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

def DFS(graph,root):
    visited = []
    stack = [root]
    
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            temp = list(set(graph[n]) - set(visited))
            stack += sorted(temp, reverse= True)
    return visited

def BFS(graph, root):
    visited = []
    queue = deque([root])
    
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            temp = list(set(graph[n]) - set(visited))
            queue += sorted(temp)
    return visited

node, edge, root = map(int, sys.stdin.readline().split())
graph_list = {}

for i in range(node):
    graph_list[i + 1] = []

for _ in range(edge):
    node1, node2 = (map(int, sys.stdin.readline().split()))
    graph_list[node1].append(node2)
    graph_list[node2].append(node1)
    
# 실패한 케이스 - 시작 root에 연결된 간선이 없을 경우 Keyerror가 뜬다.
# 위에 모든 노드를 연결해주는 방안으로 해결
# for _ in range(edge):
#     node1, node2 = (map(int, sys.stdin.readline().split()))
#     if node1 not in graph_list:
#         graph_list[node1] = [node2]
#     elif node2 not in graph_list[node1]:
#         graph_list[node1].append(node2)
        
#     if node2 not in graph_list:
#         graph_list[node2] = [node1]
#     elif node1 not in graph_list[node2]:
#         graph_list[node2].append(node1)

print(*DFS(graph_list, root))
print(*BFS(graph_list, root))


# graph_list의 형태 예시
# graph_list = {1: set([3, 4]),
#               2: set([3, 4, 5]),
#               3: set([1, 5]),
#               4: set([1]),
#               5: set([2, 6]),
#               6: set([3, 5])}