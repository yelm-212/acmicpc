import sys
from collections import deque
r = sys.stdin.readline
n = int(r())
newdeque = deque([])

for _ in range(n):
    option = r().split()
    if option[0] == 'push_front':
        newdeque.appendleft((option[1]))
    elif option[0] == 'push_back':
        newdeque.append((option[1]))
    elif option[0] == 'pop_front':
        if len(newdeque) == 0:
            print(-1)
        else:
            print(newdeque.popleft())
    elif option[0] == 'pop_back':
        if len(newdeque) == 0:
            print(-1)
        else:
            print(newdeque.pop())
    elif option[0] == 'size':
        print(len(newdeque))
    elif option[0] == 'empty':
        if len(newdeque) == 0:
            print(1)
        else:
            print(0)
    elif option[0] == 'front':
        if len(newdeque) == 0:
            print(-1)
        else:
            print(newdeque[0])
    elif option[0] == 'back':
        if len(newdeque) == 0:
            print(-1)
        else:
            print(newdeque[-1])
