import sys
r = sys.stdin.readline

N, M = map(int, r().rstrip().split())

foo = []

def DFS():
    if len(foo) == M:
        print(*foo)
        return
    
    for i in range(1, N+1):
        if foo and foo[-1]>i :
            continue
        
        foo.append(i)
        DFS()
        foo.pop()
        
DFS()