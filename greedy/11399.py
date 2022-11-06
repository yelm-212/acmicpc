import itertools
import sys

read = sys.stdin.readline

N = int(input())

plist = list(map(int, read().rstrip().split()))
plist.sort()

res = list(itertools.accumulate(plist))

print(sum(res))
