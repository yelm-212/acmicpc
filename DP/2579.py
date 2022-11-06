import sys
r = sys.stdin.readline

n = int(r())
stairs = [ int(r()) for _ in range(n) ]
DP = [0] * (n+1)

DP[0] = stairs[0] 

if len(stairs) >1:
    DP[1] = stairs[0] + stairs[1]

if len(stairs) >2:
    DP[2] = stairs[2] + max(stairs[1], stairs[0])

for i in range(3, n):
    DP[i] = stairs[i] + max(stairs[i-1] + DP[i-3] , DP[i-2])
    
print(DP[n-1])