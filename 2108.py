# https://www.acmicpc.net/problem/2108

import sys
from collections import Counter

num = []
for _ in range(N := int(sys.stdin.readline())):
    num.append(int(sys.stdin.readline()))
    
print(round(sum(num) / N))
num.sort()
print(num[N // 2])

cnt = Counter(num).most_common(2)

if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
    
print(max(num) - min(num))


# 시간초과 -> Counter 사용 X
# mode = []
# for i in set(num):  # num의 집합을 통해서 중복된 i값을 제거 [1, 1, 1, 2, 2, 3] -> (1, 2, 3)
#     mode.append([i, num.count(i)])          # 이차원 리스트로 [i값, 배열 안에 있는 i의 개수]
# mode.sort(key= lambda x : (-x[1], x[0]))    # 정렬은 i의 개수가 많을 수록, i의 값이 적을수록 정렬 [0, 0, -1] -> [[0, 2], [-1, 1]]
# print(mode)
# if len(mode) > 1:                           # mode의 개수가 1보다 많을때
#     if mode[0][1] == mode[1][1]:            # 만약 최빈값이 2개 이상이라면
#         print(mode[1][0])                   # 최빈값 중 두번째로 작은 값을 출력한다
#     else:
#         print(mode[0][0])                   # 아닐 경우 첫번째 값만 출력
# else:
#     print(mode[0][0])