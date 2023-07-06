import sys

N, M = list(map(int, sys.stdin.readline().split()))

dogam = {}

for i in range(1, N + 1):
    Name = sys.stdin.readline().strip()
    dogam[i] = Name
    dogam[Name] = i

for i in range(M):
    Q = sys.stdin.readline().strip()
    if Q.isdigit():
        print(dogam[int(Q)])
    else:
        print(dogam[Q])


# poketlist = []
# for i in range(N):
#     temp = sys.stdin.readline().strip()
#     poketlist.append(temp)

# for _ in range(M):
#     item = sys.stdin.readline().strip()
#     if item.isdigit() == True:
#         print(poketlist[int(item) - 1])
#     else:
#         print(poketlist.index(item) + 1)
        

# 실패한 케이스 - 시간초과
# for i in range(1, N + 1):
#     Name = sys.stdin.readline().strip()
#     dogam[i] = Name

# reverse_dogam = dict(map(reversed, dogam.items()))

# for _ in range(M):
#     Q = sys.stdin.readline().strip()
#     if Q.isdigit():
#         print(dogam.get(int(Q)))
#     else:
#         print(reverse_dogam.get(Q))