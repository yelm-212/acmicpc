import sys
n = int(sys.stdin.readline())
i = 2

while n != 1:
    if n % i != 0:
        i += 1
    else:
        n = n // i
        print(i)