N = int(input())

DP = [[0]*10 for _ in range(N+1)]
DP[1] = [0] + [1 for _ in range(9)]

for i in range(2,N+1):
    for j in range(10):
        if j == 0: #뒷자리가 0인 경우
            DP[i][j] = DP[i-1][j+1]
        elif j == 9: # 뒷자리가 9인 경우
            DP[i][j] = DP[i-1][j-1]
        else:
            DP[i][j] = DP[i-1][j-1] + DP[i-1][j+1]
        
print(sum(DP[N]) % 1000000000)
    