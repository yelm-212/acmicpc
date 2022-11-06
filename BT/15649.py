import sys
r = sys.stdin.readline
N, M= map(int, r().split()) 

foo = []

def dfs():
    if len(foo) == M :
        print(*foo)
        return
    
    for i in range(1, N+1):
        if i in foo : 
            continue
        
        foo.append(i)
        dfs()
        foo.pop()

dfs()