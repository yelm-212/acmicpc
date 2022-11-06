N, M = map(int, input().rstrip().split())

foo = []

def dfs():
    if len(foo) == M :
        print(*foo)
        return
    
    for i in range(1, N+1):
        foo.append(i)
        dfs()
        foo.pop()

dfs()