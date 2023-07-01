# https://www.acmicpc.net/problem/6198

import sys

N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(N)]

stack = []
cnt = 0
for n in num:
    while stack and stack[-1] <= n:
        stack.pop()

    cnt += len(stack)
    stack.append(n)
print(cnt)





# 실패한 케이스 1
# v = num.pop(0)
# stack = [v]
# cnt = 0
# while stack:
#     if len(num) != 0:
#         n = num.pop(0)
#     else:
#         n = 0
        
#     if n == 0:
#         while stack:
#             stack.pop()
#             cnt += len(stack)
#     elif n < stack[-1]:
#         stack.append(n)
#         pre = n
#     elif stack[-1] <= n < stack[0]:
#         stack.pop()
#         cnt += len(stack)
#         stack.append(n)
#     elif n >= stack[0]:
#         while stack:
#             stack.pop()
#             cnt += len(stack)
#         stack = [n]
# print(cnt)


# 실패한 케이스 2 - 반례 num = [5, 4, 3, 2, 1, 4, 3, 2, 1] - 해결
# for n in num:
#     if stack[0] <= n:         # -> while stack[-1] <= n:
#         stack = []            # ->    stack.pop()
#     elif stack[-1] > n:
#         cnt += len(stack)
#     elif stack[-1] <= n:
#         stack.pop()
#         cnt += len(stack)
#     stack.append(n)
# print(cnt)