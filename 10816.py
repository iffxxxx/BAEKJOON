# https://www.acmicpc.net/problem/10816

import sys
from collections import Counter

N = int(sys.stdin.readline())
Sang = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Card = list(map(int, sys.stdin.readline().split()))

counter = Counter(Sang)
for i in Card:
    print(counter[i], end = " ")