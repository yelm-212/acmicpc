from collections import deque
import sys
r = sys.stdin.readline
T = int(r())

for _ in range(T):
    N, M = map(int, r().split())
    pqueue = deque(list(map(int, r().split())))
    # printq = enumerate(printlist, start=1)
    # print(*printq)
    cnt = 0
    while pqueue: 
        pmax = max(pqueue)
        temp = pqueue.popleft()
        M -= 1
        if temp == pmax:
            cnt+=1
            if M < 0: break
        else:
            pqueue.append(temp)
            if M<0: 
                M= len(pqueue) -1

    print(cnt)

            
    