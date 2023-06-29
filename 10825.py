# https://www.acmicpc.net/problem/10825

import sys

score = []
for _ in range(int(sys.stdin.readline())):
    score.append(list((sys.stdin.readline().split())))
    
score.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in score:
    print(i[0])