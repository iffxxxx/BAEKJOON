# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/1157

temp = list(input())

dp = [0] * 26

for t in temp:
    t = t.upper()
    dp[ord(t) - 65] += 1
    
cnt = max(dp)
answer = []
for i in range(26):
    if dp[i] == cnt:
        answer.append(i)

if len(answer) == 1:
    print(chr(answer[0] + 65))
else:
    print("?")