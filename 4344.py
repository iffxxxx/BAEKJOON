# https://www.acmicpc.net/problem/4344

import sys

num = []
for i in range(int(sys.stdin.readline())):
    num.append(list(map(int, sys.stdin.readline().split())))
        
for i in num:
    aver = sum(i[1:]) / i[0]
    cnt = 0
    for j in i[1:]:
        if j > aver:
            cnt += 1
    print("{:.3f}".format(100 * cnt / i[0]) + "%")