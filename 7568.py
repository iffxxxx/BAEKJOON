# https://www.acmicpc.net/problem/7568

import sys

N = int(input())
people = []
for _ in range(N):
    people.append(list(map(int, (sys.stdin.readline().split()))))

for w, h in people:
    rank = 1
    for m, n in people:
        if w < m and h < n:
            rank += 1
    print(rank, end = " ")


# 인덱스로 해결

# import sys

# N = int(input())
# people = []
# for i in range(N):
#     people.append(list(map(int, (sys.stdin.readline().split()))))
# weight = sorted([i for i in people], key= lambda x: (x[0], x[1]), reverse= True)
# height = sorted([i for i in people], key= lambda x: (x[1], x[0]), reverse= True)

# answer = []
# dictionary = {tuple(x): 0 for x in people}
# for j in people:
#     w = weight.index(j)
#     h = height.index(j)
#     for m in range(min(w, h), max(w, h) + 1):
#         dictionary[tuple(weight[m])] = min(w, h) + 1
# print(*[dictionary[i] for i in dictionary])