import sys

r = sys.stdin.readline

N, K = map(int, r().rstrip().split())

def multiply(n, mult):
    if mult == 1:
        return n
    else:
        return n * multiply(n-1, mult-1)

def calculate(n, k):
    half = n // 2
    
    if k == 0: 
        print(1)
    elif k> half: 
        calculate(n, n-k)
    else:
        print((multiply(n, k) // multiply(k, k)) % 10007)
        
calculate(N, K)