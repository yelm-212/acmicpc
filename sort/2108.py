import sys
from collections import Counter
r = sys.stdin.readline

N = int(r())
inputlist = [ int(r()) for _ in range(N)]
inputlist.sort()

cntlist = Counter(inputlist).most_common()

print(round(sum(inputlist)/N))
print(inputlist[N//2])

if len(cntlist) == 1:
    print(cntlist[0][0])
elif cntlist[0][1] == cntlist[1][1]:
    print(cntlist[1][0])
else:
    print(cntlist[0][0])

print(inputlist[-1]-inputlist[0])