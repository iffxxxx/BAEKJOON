# https://www.acmicpc.net/problem/3040

import sys

dwarf = []
for _ in range(9):
    dwarf.append(int(sys.stdin.readline()))
    
onehund = sum(dwarf)
Okay = True
for i in range(9):
    for j in range(9):
        if i != j:
            a = dwarf[i]
            b = dwarf[j]
            if onehund - a - b == 100:
                dwarf.remove(a)
                dwarf.remove(b)
                Okay = False
                break
    if(Okay == False):
        break

for d in dwarf:
    print(d)