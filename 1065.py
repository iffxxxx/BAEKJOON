# � ���� ���� X�� �� �ڸ��� ���������� �̷�ٸ�, �� ���� �Ѽ���� �Ѵ�.
# ���������� ���ӵ� �� ���� ���� ���̰� ������ ������ ���Ѵ�.
# N�� �־����� ��, 1���� ũ�ų� ����, N���� �۰ų� ���� �Ѽ��� ������ ����ϴ� ���α׷��� �ۼ��Ͻÿ�. 

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