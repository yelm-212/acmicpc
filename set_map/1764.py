import sys
r = sys.stdin.readline

N, M= map(int, r().strip().split()) 

heard = set([r().strip() for _ in range(N)])
seen = set([r().strip() for _ in range(M)])

newset = list(heard & seen)

print(len(newset))
newset.sort()
print(*newset, sep = "\n")