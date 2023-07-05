# https://www.acmicpc.net/problem/2003

import sys

N, M = list(map(int, sys.stdin.readline().split()))
num = [0] + list(map(int, sys.stdin.readline().split()))

for n in range(1, N + 1):
    num[n] += num[n - 1]

# 투포인트
cnt = 0
left, right = 0, 1
while left <= right < N + 1:
    if num[right] - num[left] == M:
        cnt += 1
        right += 1
    elif num[right] - num[left] < M:
        right += 1
    else:
        left += 1
print(cnt)


# 실패한 케이스 1 - 시간초과
# cnt = 0
# start = 0
# for i in range(start, N + 1):
#     for j in range(start, i):
#         if num[i] - num[j] == M:
#             cnt += 1
#             start = j
#             break
# print(cnt)