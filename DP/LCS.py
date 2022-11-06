A = input().rstrip()
B = input().rstrip()

def LCS(A, B):
    m, n = len(A), len(B)
    L = [[None]*(n+1) for i in range(m+1)]
 
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif A[i-1] == B[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    # L[m][n] => length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]

print(LCS(A, B))

