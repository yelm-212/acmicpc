import sys
r = sys.stdin.readline

N = int(r())
inputlist = set([int(r()) for _ in range(N)])
inputlist.sort(key = lambda x: (len(x), x))

print(*inputlist)