import sys
r = sys.stdin.readline

N = int(r())
inputlist = [list(map(int, r().split())) for _ in range(N)]
inputlist.sort(key = lambda x: (x[1], x[0]))

for point in inputlist: print(*point)