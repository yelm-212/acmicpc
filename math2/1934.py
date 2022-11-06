import sys
r = sys.stdin.readline

def GCD(X, Y):
    while Y:
        X, Y = Y, X % Y

    return X

def LCM(X, Y):
    return X*Y // GCD(X, Y)

T = int(r())
for _ in range(T):
    A, B = map(int, input().rstrip().split())
    print(LCM(A, B))