import sys
import math

p = int(1e9) + 7
n, k = map(int, (sys.stdin.readline().split()))


def factorial(n: int):
    result = 1
    for i in range(1, n + 1):
        result *= i
        result %= p
    return result


def exp(base: int, expo: int):
    if expo == 1:
        return base
    a = exp(base, expo // 2)
    b = expo % 2
    return a * a * (base**b) % p


print((factorial(n)) % p * exp((factorial(k)) * (factorial(n - k)), p - 2) % p)
