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


# �ð��ʰ� -> Counter ��� X
# mode = []
# for i in set(num):  # num�� ������ ���ؼ� �ߺ��� i���� ���� [1, 1, 1, 2, 2, 3] -> (1, 2, 3)
#     mode.append([i, num.count(i)])          # ������ ����Ʈ�� [i��, �迭 �ȿ� �ִ� i�� ����]
# mode.sort(key= lambda x : (-x[1], x[0]))    # ������ i�� ������ ���� ����, i�� ���� �������� ���� [0, 0, -1] -> [[0, 2], [-1, 1]]
# print(mode)
# if len(mode) > 1:                           # mode�� ������ 1���� ������
#     if mode[0][1] == mode[1][1]:            # ���� �ֺ��� 2�� �̻��̶��
#         print(mode[1][0])                   # �ֺ� �� �ι�°�� ���� ���� ����Ѵ�
#     else:
#         print(mode[0][0])                   # �ƴ� ��� ù��° ���� ���
# else:
#     print(mode[0][0])