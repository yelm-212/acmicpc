N, M = map(int, input().rstrip().split())

foo = []

def dfs():
    if len(foo) == M :
        print(*foo)
        return
    
    for i in range(1, N+1):
        if i in foo : 
            continue
        if foo and i <= foo[-1]: 
            continue
        
        foo.append(i)
        dfs()
        foo.pop()

dfs()