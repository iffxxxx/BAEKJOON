# ù° �ٿ� �ڿ��� N(1 �� N �� 100,000)�� �־�����.
# ���� �ٿ��� N���� ���� A[1], A[2], ��, A[N]�� �־�����. ���� �ٿ��� M(1 �� M �� 100,000)�� �־�����.
# ���� �ٿ��� M���� ������ �־����µ�, �� ������ A�ȿ� �����ϴ��� �˾Ƴ��� �ȴ�. ��� ������ ������ -231 ���� ũ�ų� ���� 231���� �۴�.

import sys

n = int(input())
A = list(map(int, (sys.stdin.readline().split())))
A = set(A[:n])
m = int(input())
M = list(map(int, (sys.stdin.readline().split())))
M = M[: m]

for i in M:
    print(1) if i in A else print(0)