import sys
r = sys.stdin.readline

N = int(r())
inputlist =  [ int(r()) for _ in range(N)]

inputlist.sort()

print(*inputlist, sep="\n")