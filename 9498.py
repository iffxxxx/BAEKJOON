# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/9498

n = int(input())

if 90 <= n <= 100:
    print("A")
elif 80 <= n < 90:
    print("B")
elif 70 <= n < 80:
    print("C")
elif 60 <= n < 70:
    print("D")
else:
    print("F")