import sys
r = sys.stdin.readline

N = int(r())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def calc():
    nF = factorial(N)
    if nF % 10 == 0:
        strnF = list(str(nF))
        cnt = 0
        
        for i in strnF[::-1]:
            if i == "0":
                cnt +=1
            else:
                break
        
        return cnt
            
    else:
        return 0
    
print(calc())