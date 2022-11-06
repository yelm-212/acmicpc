import sys

read = sys.stdin.readline

N, B = map(int, read().rstrip().split())
A = [list(map(int, read().rstrip().split())) for _ in range(N)]


def mat_mult(A: list, B: list) -> list:
    n = len(A)
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmpval = 0
            for k in range(n):
                tmpval += A[i][k] * B[k][j]
            temp[i][j] = tmpval % 1000
    return temp


def mat_pow(A: list, n: int) -> list:
    if n == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    if n % 2 == 0:
        temp = mat_pow(A, n // 2)
        return mat_mult(temp, temp)
    else:
        temp = mat_pow(A, n - 1)
        return mat_mult(temp, A)


res = mat_pow(A, B)
for i in res:
    print(*i)
