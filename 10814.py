# https://www.acmicpc.net/problem/10814

import sys

N = int(input())
num = []
for _ in range(N):
    num.append((sys.stdin.readline().split()))
    
num.sort(key = lambda x : int(x[0])) # str�� int�� ��ȯ�ϰ� ����
for i in num:
    print(i[0], i[1])