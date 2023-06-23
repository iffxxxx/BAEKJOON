# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다.
# 수는 중복되지 않는다.

import sys

n = int(input())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

for i in sorted(num):
    print(i)


# 실패한 케이스 - 시간초과 - N의 값이 1,000,000일 경우 for문에서 시간초과
# N = int(input())

# tem = []
# for i in range(0, N):
#     num = int(input())
#     tem.append(num)
    
# for j in sorted(tem):
#     print(j)