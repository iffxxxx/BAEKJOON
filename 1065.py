# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

def solution(N):
    tem = [i for i in range(1,100)]
    for i in range(1,10):
        for j in range(0,5):
            if i + 2 * j < 10:
                temp = str(i) + str(i + j) + str(i + 2 * j)
                tem.append(int(temp))
            if i - 2 * j >= 0:
                temp = str(i) + str(i - j) + str(i - 2 * j)
                tem.append(int(temp))
    tem = set(sorted(tem))
    return len([i for i in tem if i <= N])

N = int(input())
print(solution(N))