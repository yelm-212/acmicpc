import sys
r = sys.stdin.readline

n = int(r())
DP = [ list(map(int, r().rstrip().split())) for _ in range(n)]

step = 2

for i in range(1,n):
    for j in range(step):
        if j == 0:
            DP[i][j] = DP[i][j] + DP[i-1][j]
        elif i == j:
            DP[i][j] = DP[i][j] + DP[i-1][j-1]
        else:    
            DP[i][j] = DP[i][j] + max(DP[i-1][j-1], DP[i-1][j])
            
    step += 1
    
print(max(DP[n-1]))
            