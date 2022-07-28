import sys
r = sys.stdin.readline

N = int(r())

stack = []

for _ in range(N):
    temp = r().strip()
    if "push" in temp:
        X = int(temp[5:])
        stack.append(X)
    elif "pop" in temp:
        if len(stack) == 0 : print(-1)
        else: print(stack.pop())
    elif "size" in temp:
        print(len(stack))
    elif "empty" in temp:
        if len(stack): print(0)
        else : print(1) # len(stack) == 0
    elif "top" in temp:
        if len(stack) == 0 : print(-1)
        else: print(stack[-1])
