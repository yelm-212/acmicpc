import sys
r = sys.stdin.readline

N = int(r())
nlist = [int(r()) for _ in range(N)]
DP = [0] * (N)

DP[0] = nlist[0]

if len(nlist) > 1:
    DP[1] = nlist[0] + nlist[1]

if len(nlist) > 2:
    DP[2] = max(DP[1], nlist[0] + nlist[2], nlist[1] + nlist[2])

for i in range(3, N):
    DP[i] = max(DP[i-1], DP[i-2] + nlist[i] , DP[i-3] + nlist[i-1] + nlist[i])
    
print(DP[N-1])