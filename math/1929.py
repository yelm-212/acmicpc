import sys

def Primechecker(n):
    if n == 1:
        return False
    
    for i in range(2, int(n**0.5)+1): # 루트값만 돌려줘도 판정 가능
        if n%i ==0: return False
            
    return True

M, N = map(int, sys.stdin.readline().split())

for i in range (M, N+1):
    if Primechecker(i):
        print(i)
