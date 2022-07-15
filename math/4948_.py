import sys
r = sys.stdin.readline

def Primechecker(n):
    if n == 1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n%i ==0: return False
            
    return True
    
while True:
    N = int(r())
    cnt = 0
    
    if N == 0: break

    for i in range(N+1, 2*N+1):
        if Primechecker(i): cnt +=1
        
    print(cnt)