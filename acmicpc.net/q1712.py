import sys
r = sys.stdin.readline

a, b, c = map(int, r().split())
if (c-b) <= 0:
    print(-1)
else:
    print(int((a)/(c-b)+1))