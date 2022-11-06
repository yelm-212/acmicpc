import sys
r = sys.stdin.readline

N, K = map(int, r().rstrip().split())
items = [list(map(int, r().rstrip().split())) for _ in range(N)]

def Knapsack():
    DP = [0]*(K+1)

    for i in range(1, N+1):
        for w in range(K, 0, -1):
            if items[i-1][0] <= w : 
                DP[w] = max(DP[w], DP[w-items[i-1][0]]+items[i-1][1])
                
    return DP[K] 
    # returns maximum val. of knapsack

print(Knapsack())