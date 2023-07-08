# https://www.acmicpc.net/problem/2493

import sys

N = int(sys.stdin.readline())
Top = list(map(int, sys.stdin.readline().split()))

answer = [0] * N
stack = []          # stack에는 수신을 받는 타워의 인덱스가 들어간다

for i in range(N):
    cur = Top[i]
    while stack and Top[stack[-1]] < cur:   # 수신을 받지 못하는 타워의 인덱스는 지워진다.
        stack.pop()
    if stack:
        answer[i] = stack[-1] + 1           # 수신을 보내는 타워에 stack의 마지막 원소가 대입된다
    stack.append(i)

print(*answer)

# 실패한 케이스 - 시간초과
# while Top:
#     flag = True
#     cur = Top.pop()
#     for i in range(-1, -(len(Top) + 1), -1):
#         if Top[i] > cur:
#             answer = [len(Top) + i + 1] + answer
#             flag = False
#             break
    
#     if flag:
#         answer = [0] + answer

# print(*answer)