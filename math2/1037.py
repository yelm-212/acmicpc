import sys
r = sys.stdin.readline

n = int(r())
nlist = list(map(int, r().rstrip().split()))
nlist.sort()

print(nlist[0] * nlist[-1])