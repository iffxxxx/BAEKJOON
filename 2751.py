# ù° �ٿ� ���� ���� N(1 �� N �� 1,000,000)�� �־�����.
# ��° �ٺ��� N���� �ٿ��� ���� �־�����. �� ���� ������ 1,000,000���� �۰ų� ���� �����̴�.
# ���� �ߺ����� �ʴ´�.

import sys

n = int(input())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

for i in sorted(num):
    print(i)


# ������ ���̽� - �ð��ʰ� - N�� ���� 1,000,000�� ��� for������ �ð��ʰ�
# N = int(input())

# tem = []
# for i in range(0, N):
#     num = int(input())
#     tem.append(num)
    
# for j in sorted(tem):
#     print(j)