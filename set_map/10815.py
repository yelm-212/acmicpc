import sys
r = sys.stdin.readline

N = int(r())
sack = set(list(map(int, r().split()))) # 유무만 확인하면 되므로 set
M = int(r())
check = list(map(int, r().split()))

for checklist in check:
    if checklist in sack : print("1",end = " ")
    else: print ("0",end = " ")