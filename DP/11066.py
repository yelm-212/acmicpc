import sys

r = sys.stdin.readline

T = int(r())
for i in range(T):
    K = int(r())
    sizeList = list(map(int, r().split()))
    DP = [0] * K
