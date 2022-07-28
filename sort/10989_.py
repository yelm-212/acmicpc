import sys
r = sys.stdin.readline
N = int(r())
nlist = [0 for _ in range(10001)]

for _ in range(N):
    nlist[int(r())] +=1

for i in range(10001):
    if not nlist[i] == 0:
        for _ in range(nlist[i]): print(i)

