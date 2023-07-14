# https://www.acmicpc.net/problem/1010 다리 놓기

import sys

def fact(A):
    cnt = 1
    for i in range(1, A + 1):
        cnt *= i
    return cnt

for t in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    print(fact(M) // (fact(N) * fact(M - N)))