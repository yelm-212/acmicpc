import sys
r = sys.stdin.readline

N = int(r())
stack = []

for _ in range(N):
    temp = int(r().strip())
    if temp != 0:
        stack.append(temp)
    else:
        stack.pop()
print(sum(stack))