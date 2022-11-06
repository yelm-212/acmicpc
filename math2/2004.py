import sys
sys.setrecursionlimit(10**6)
r = sys.stdin.readline

N, M = map(int, r().rstrip().split())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def comb(n, k):    
    if k == 0: 
        return 1
    elif k > (n // 2): 
        comb(n, n-k)
    else:
        return factorial(n) // (factorial(k) * factorial(n-k))

def calc():
    nF = comb(N, M)
    if nF % 10 == 0:
        strnF = str(nF)
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