# https://www.acmicpc.net/problem/1057 토너먼트

import sys

N, A, B = map(int,sys.stdin.readline().split())

cnt = 0
while A != B:
    A -= A // 2
    B -= B // 2
    cnt += 1
print(cnt)




# 실패한 케이스 1 - 23781 15127 15461 => 정답 11 결과값 9
# i = 1
# while True:
#     if 2 ** i <= N < 2 ** (i + 1):
#         n = i + 1   # n은 나올 수 있는 최대 라운드 수
#         break
#     i += 1

# a = min(A, B)
# b = max(A, B)
# half = 2 ** (n - 1)
# if a > half and b > half:   # 오른쪽의 수들을 half 만큼 빼주어 왼쪽으로 이동 - 나눗셈이 용이해짐
#     a -= half
#     b -= half

# for j in range(1, n + 1):
#     if a <= 2 ** (n - j) < b:
#         print(n - j + 1)
#         break
#     elif 2 ** (j - 1) <= b - a < 2 ** j:
#         print(j)
#         break


# 실패한 케이스 2 - 시간초과
# i = 1
# while True:
#     if 2 ** i < N <= 2 ** (i + 1):
#         n = i + 1   # n은 나올 수 있는 최대 라운드 수
#         break
#     i += 1

# a = min(A, B)
# b = max(A, B)

# for j in range(1, n + 1):
#     half = 2 ** (n - j)
#     if a <= half < b:
#         print(n - j + 1)
#         break

#     elif a > half and b > half:   # 오른쪽의 수들을 half 만큼 빼주어 왼쪽으로 이동 - 나눗셈이 용이해짐
#         a -= half
#         b -= half
#         if a > half // 2 and b <= half:
#             a -= half // 2
#             b -= half // 2