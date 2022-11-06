import sys
r = sys.stdin.readline

N = int(r())
stat = [list(map(int, r().rstrip().split())) for _ in range(N)]
minimum = 10000000
visited = [False] * (N+1)

def DFS(D, idx):
    global minimum
    if D == (N//2) :
        S, L = 0, 0 
        for i in range(N): 
            for j in range(i+1,N): 
                if visited[i] and visited[j]: 
                    S += (stat[i][j] + stat[j][i])
                elif not visited[i] and not visited[j]: 
                    L += (stat[i][j] + stat[j][i]) 
        minimum = min(minimum, abs(S - L))

    for i in range(idx, N):
        if not visited: 
            visited[i] = True
            DFS(D+1, i+1)
            visited[i] = False
            
DFS(0, 0)
print(minimum)
