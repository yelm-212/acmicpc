import sys
r = sys.stdin.readline

N = int(r())
A_B = [list(map(int, r().rstrip().split())) for _ in range(N)]
A_B.sort(key=lambda x: x[0]) #A기준 정렬

def ascending():
    # check ascending order in DP
    DP = [0]*(N)
    
    B = [A_B[i][1] for i in range(N)] 
    
    for i in range(N):
        for j in range(i):
            if B[i] > B[j] and DP[i]<DP[j]: 
                DP[i] = DP[j]
        DP[i] +=1
    
    return N - max(DP) # calculated val.

print(ascending())