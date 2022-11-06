from collections import deque
N, K = map(int, input().split())

nlist = deque(list(range(1,N+1)))
plist = []

while nlist:
    nlist.rotate(0-K+1)
    plist.append(nlist.popleft())
    
print("<", end="")
print(*plist, sep = ", ", end ="")
print(">", end="")