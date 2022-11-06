import sys
r = sys.stdin.readline

N = int(r())

f = [0]* (N+1)

cnt1 = 1
cnt2 = 0

def fib(n) :
    global cnt1
    cnt1 +=1
    if n == 1 or n == 2:
        cnt1 -=1
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))


def fibonacci(n):
    global cnt2
    f[1] = 1
    f[2] = 1
    for i in range(3, N+1):
        cnt2 +=1
        f[i] = f[i - 1] + f[i - 2];  # 코드2
    return f[n];

fib(N)

fibonacci(N)

print(cnt1, cnt2)
