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
    
    # 1 2 2 1 3 3 4 5 2 1 (TC1)
    return DP

def descending():
    # check descending order in DP
    DP = [1]*(N)
    A.reverse()

    for i in range(N):
        for j in range(i):
            if A[i] > A[j]: 
                DP[i] = max(DP[i], DP[j]+1)
    
    DP.reverse()
    # 1 5 2 1 4 3 3 3 2 1 (TC1)
    return DP
    

def check():
    DP_a = ascending()
    DP_b = descending()
    
    DP = [DP_a[i] + DP_b[i] for i in range(N)]
    
    return max(DP) # calculated twice

print(check()-1)