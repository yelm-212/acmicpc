A, B, C = map(int, input().rstrip().split())


def pow(a, n):
    if n == 1:
        return a % C

    else:
        tmp = pow(a, n // 2)  # recursion
        if (n % 2 == 0):
            return tmp * tmp % C
        else:
            return a * tmp * tmp % C


print(pow(A, B))
