import sys

r = sys.stdin.readline

T = int(r())

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
        print(multiply(n, k) // multiply(k, k))
        
for _ in range(T):
    N, M = map(int, r().rstrip().split())
    calculate(M, N)