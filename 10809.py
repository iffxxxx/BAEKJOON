# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/10809

import sys

S = list(input())
answer = [-1] * 26

for i, s in enumerate(S):
    if answer[ord(s) - 97] == -1:
        answer[ord(s) - 97] = i

print(*answer)