import sys
r = sys.stdin.readline

N = int(r())
nlist = list(map(int, r().rstrip().split()))

for i in range(1, N):
    nlist[i] = max(nlist[i], nlist[i-1]+ nlist[i])
    
print(max(nlist))