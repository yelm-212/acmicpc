import sys
r = sys.stdin.readline

NA, NB= map(int, r().strip().split()) 

A = set(map(int, r().strip().split()) )
B = set(map(int, r().strip().split()) )

print(len(A - B) + len(B - A))