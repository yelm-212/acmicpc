from collections import deque
N = int(input())

nlist = deque(list(range(1,N+1)))

while len(nlist) != 1:
    nlist.popleft()
    nlist.rotate(-1)
    
print(*nlist)