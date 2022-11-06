import sys
from collections import deque
r = sys.stdin.readline

def GCD(X, Y):
    while Y:
        X, Y = Y, X % Y

    return X

N = int(r())
nlist = deque(list(map(int, r().rstrip().split())))

X = nlist.popleft()

for num in nlist:
    gcd = GCD(num, X)
    print(str(X // gcd)+"/"+str(num // gcd))