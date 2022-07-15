import sys
r = sys.stdin.readline
# 범위 주의 ㅋㅋ 바보 ㅠㅜ

def Primechecker(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i ==0:
                return False
            
        return True

list = [0 for _ in range(123456*2+1)] # 0부터 Nmax*2까지 list 생성 후 미리 primecheck 돌림(dp)

for i in range(123456*2+1):
    if Primechecker(i): list[i] = 1

while True:
    N = int(r())
    cnt = 0
    
    if N == 0: 
        break
    if N == 1: 
        cnt = 1
    
    for idx in list[N+1:2*N]:
        if idx == 1:
            cnt+=1

        
    print(cnt)
    