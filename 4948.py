# https://www.acmicpc.net/problem/4948

num = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        num.append(n)

is_prime = [True] * (m := 2 * 123456 + 1)
is_prime[0] = is_prime[1] = False
primes = []
for i in range(2, m):
    if is_prime[i]:
        primes.append(i)
        for j in range(2 * i, m, i):
            is_prime[j] = False
print(is_prime)
            
for q in num:
    print(sum(is_prime[q + 1 : 2 * q + 1]))