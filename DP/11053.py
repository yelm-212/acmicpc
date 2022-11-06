import sys
r = sys.stdin.readline

N = int(r())
A = list(map(int, r().rstrip().split()))

def ascending():
    # check ascending order in DP
    DP = [1]*(N)
    for i in range(N):
        for j in range(i):
            if A[i] > A[j]: 
                DP[i] = max(DP[i], DP[j]+1)
    
    # 10 20 10 30 20 50 (TC1)
    return DP
    

def check():
    DP = ascending()
    return max(DP) # calculated val.

print(check())