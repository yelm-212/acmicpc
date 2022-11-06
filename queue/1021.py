from collections import deque
import sys
r = sys.stdin.readline

N, M = map(int, r().split())
poplist = list(map(int, r().split()))
nlist = deque(list(range(1, N+1)))

cnt = 0

for target in poplist:
    while True:
        targetidx =  nlist.index(target)
        if nlist[0] == target: 
            nlist.popleft()
            break
        else:
            if targetidx <= (len(nlist) // 2):
                nlist.rotate(-1)
            else:
                nlist.rotate(1)
            cnt += 1

print(cnt)