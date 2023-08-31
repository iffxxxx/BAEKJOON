# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/9663

N = int(input())

dp = [0] * N
cnt = 0

def possible(x):
    for i in range(x):
        if dp[x] == dp[i] or abs(dp[x] - dp[i]) == abs(x - i):
            return False
    return True
    
def BACK(x):
    global cnt
    
    if x == N:
        cnt += 1
        return
    
    else:
        for i in range(N):
            dp[x] = i   # 첫번째 줄부터 처리

            if possible(x):
                BACK(x + 1)

BACK(0)
print(cnt)