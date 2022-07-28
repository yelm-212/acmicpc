import sys
r = sys.stdin.readline

N = int(r())
inputlist = []

for _ in range(N):
    age, name = r().split()
    inputlist.append((int(age), name))
    
inputlist.sort(key = lambda x:x[0])

for point in inputlist: print(*point)