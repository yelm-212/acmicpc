M = int(input())
N = int(input())

def Primechecker(n):
    if n == 1:
        return False
    
    for i in range(2, n):
        if n%i ==0: return False
        
    return True

list = []

for i in range(M,N+1): #범위 주의
    if Primechecker(i):
        list.append(i)

if not list:
    print("-1")
else:
    print(sum(list))
    print(min(list))
    