# https://www.acmicpc.net/problem/1011

import sys

num = []
for _ in range(int(input())):
    num.append(sys.stdin.readline().split())
    
tem = [int(i[1]) - int(i[0]) for i in num]

for t in tem:
    x = int(t ** 0.5)
    if t == x ** 2:
        print(2 * x - 1)
    elif t <= x * (x + 1):
        print(2 * x)
    elif t > x * (x + 1):
        print(2 * x + 1)