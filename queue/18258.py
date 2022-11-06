from collections import deque
import sys
r = sys.stdin.readline
N = int(r())
q = deque()

for _ in range(N):
    temp = r().strip()
    if "push" in temp:
        X = int(temp[5:])
        q.append(X)
    elif "pop" in temp:
        if len(q) == 0 : print(-1)
        else: print(q.popleft())
    elif "size" in temp: print(len(q))
    elif "empty" in temp:
        if len(q): print(0)
        else : print(1) # len(q) == 0
    elif "front" in temp:
        if len(q) == 0 : print(-1)
        else: print(q[0])
    elif "back" in temp:
        if len(q) == 0 : print(-1)
        else: print(q[-1])