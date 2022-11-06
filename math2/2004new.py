import sys
r = sys.stdin.readline

N, M = map(int, r().rstrip().split())

def cnt2(n):
    cnt = 0
    while n!= 0:
        n = n//2
        cnt+=n
    return cnt        

def cnt5(n):
    cnt = 0
    while n!= 0:
        n = n//5
        cnt+=n
    return cnt        

def calc():
    cnt_2 = cnt2(N) - cnt2(N-M) - cnt2(M)
    cnt_5 = cnt5(N) - cnt5(N-M) - cnt5(M)
    
    return min(cnt_2, cnt_5)
    
print(calc())