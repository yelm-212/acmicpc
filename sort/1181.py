import sys
r = sys.stdin.readline

N = int(r())
inputlist = list(set([r().strip() for _ in range(N)]))
inputlist.sort(key = lambda x: (len(x), x))

print(*inputlist, sep="\n")