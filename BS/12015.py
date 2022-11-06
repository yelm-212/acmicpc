import sys
from bisect import bisect_left
r = sys.stdin.readline

N = int(r())
A = list(map(int, r().rstrip().split()))
res = [0]

for i in A:
    if res[-1] < i:
        res.append(i)
    else:
        res[bisect_left(res, i)] = i

print(len(res)-1)