# https://www.acmicpc.net/problem/1717

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# �θ� ���̺� ����
# parent = [i for i in range(N + 1)]
parent = [0] * (N + 1)
for i in range(N + 1):
    parent[i] = i

# ã�� ����
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# ������ ����
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    opr, a, b = map(int, input().split())
    if opr == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")