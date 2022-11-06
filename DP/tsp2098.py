import sys
r = sys.stdin.readline

inf = 123456789

N = int(r())
W = [list(map(int, r().rstrip().split())) for _ in range(N)]

DP = [ [ -1 for _ in range(1<<N)] for _ in range(N)]

def TSP(now,visited):
    if visited == (1<<N)-1:
        if W[now][0]: 
            return W[now][0]
        return inf
    
    if DP[now][visited] != -1: 
        return DP[now][visited]
 
    DP[now][visited] = inf

    for i in range(N):
        prom = visited|(1<<i)
        if not visited&(1<<i) and W[now][i]:
            if DP[now][visited] >= TSP(i, prom) + W[now][i]:
                DP[now][visited] = TSP(i, prom) + W[now][i]
                
    return DP[now][visited]
        
print(TSP(0,1))