# https://www.acmicpc.net/problem/10610

N = list(input())

M = [int(i) for i in N]
M.sort(reverse= True)
if sum(M) % 3 != 0 or M[-1] != 0:
    print(-1)
else:
    for m in M:
        print(m, end = "")