# # https://www.acmicpc.net/problem/28298

import sys

Mat = []
N, M, K = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    Mat.append([i for i in input()])

Sum = 0
for y in range(K):
    for x in range(K):
        
        alpha = [0] * 26    # 알파벳 개수 세기
        for dy in range(0, N, K):
            for dx in range(0, M, K):
                m = Mat[y + dy][x + dx]
                alpha[ord(m) - 65] += 1
                
        max_alpha = max(alpha)
        Sum += N * M // K ** 2 - max_alpha
        mat_alpha = chr(alpha.index(max_alpha) + 65)
        
        for dy in range(0, N, K):
            for dx in range(0, M, K):
                Mat[y + dy][x + dx] = mat_alpha

# 출력
print(Sum)
for i in Mat:
    print(''.join(i))

# 실패한 케이스 1
# import sys

# mat = []
# N, M, K = list(map(int, sys.stdin.readline().split()))
# for i in range(N):
#     mat.append([i for i in input()])

# panel = []
# answer = []
# for n in range(N // K):
#     for m in range(M // K):
#         panel = []
#         for col in range(n * K, n * K + K):
#             panel2 = []
#             for row in range(m * K, m * K + K):
#                 panel2.append(mat[col][row])
#             panel.append(panel2)
#         cnt = 0
#         for y in range(N):
#             for x in range(M):
#                 if mat[y][x] != panel[y % K][x % K]:
#                     cnt += 1
#         answer.append([cnt, panel])

# answer.sort()

# fpanel = answer[0][1]
# for y in range(N):
#     for x in range(M):
#         if mat[y][x] != fpanel[y % K][x % K]:
#             mat[y][x] = fpanel[y % K][x % K]
# print(answer[0][0])

# for i in mat:
#     print("".join(i))


# 실패한 케이스 2 - 시간 초과
# 패널 생성
# for n in range(N // K):
#     for m in range(M // K):
#         panel = []
#         for col in range(n * K, n * K + K):
#             panel.append(mat[col][m * K: m * K + K])
#         answer.append([0, panel])

# 패널과 원본 행렬 비교
# for i in range(len(answer)):
#     cnt = 0
#     for y in range(N):
#         for x in range(M):
#             if mat[y][x] != answer[i][1][y % K][x % K]:
#                 cnt += 1
#     answer[i][0] = cnt

# print(answer)

# fpanel = answer[0][1]
# for y in range(N):
#     for x in range(M):
#         if mat[y][x] != fpanel[y % K][x % K]:
#             mat[y][x] = fpanel[y % K][x % K]

# print(answer[0][0])

# for i in mat:
#     print("".join(i))
