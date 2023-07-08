# https://www.acmicpc.net/problem/2493

import sys

N = int(sys.stdin.readline())
Top = list(map(int, sys.stdin.readline().split()))

answer = [0] * N
stack = []          # stack���� ������ �޴� Ÿ���� �ε����� ����

for i in range(N):
    cur = Top[i]
    while stack and Top[stack[-1]] < cur:   # ������ ���� ���ϴ� Ÿ���� �ε����� ��������.
        stack.pop()
    if stack:
        answer[i] = stack[-1] + 1           # ������ ������ Ÿ���� stack�� ������ ���Ұ� ���Եȴ�
    stack.append(i)

print(*answer)

# ������ ���̽� - �ð��ʰ�
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