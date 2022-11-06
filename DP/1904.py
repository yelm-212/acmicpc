# 01 타일
DP = [0]*10000001

N = int(input())

DP[1] = 1
DP[2] = 2

for i in range(3, N+1):
    DP[i] = (DP[i-1] + DP[i-2]) % 15746
    
print(DP[N])
