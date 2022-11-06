import sys
r = sys.stdin.readline

N = int(r())
sack = list(map(int, r().split())) # 유무만 확인하면 되므로 set
sack.sort()

M = int(r())
check = list(map(int, r().split()))

dic = {}

for card in sack:
    if card in dic: dic[card] +=1
    else : dic[card] = 1

for checklist in check:
    if checklist in dic : 
        print(dic[checklist],end = " ")
    else: print ("0",end = " ")
    