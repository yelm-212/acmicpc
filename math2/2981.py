import sys
r = sys.stdin.readline

def GCD(X, Y):
    while Y:
        X, Y = Y, X % Y

    return X

def findM(X):
    M = set() # 중복
    M.add(X)
    for i in range(2, int(X**0.5)+1):
        if X % i == 0:
            M.add(i)
            M.add(X // i)
            
    return sorted(list(M))

N = int(r())
nlist = sorted([int(r()) for _ in range(N)])

D = []
for i in range(1, N):
    D.append(nlist[i] - nlist[i-1])
D.sort()
    

while len(D) != 1 :
    n = len(D)
    for i in range(1, n):
        D[i-1] = GCD(D[i], D[i-1])
    D = D[:n-1]

print(*findM(D[0]))