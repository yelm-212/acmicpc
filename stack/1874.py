import sys
r = sys.stdin.readline

N = int(r())
numlist = [int(r()) for _ in range(N)]
numstack = []
opstack = []
cnt = 1
flag = True

for i in range(N):
    temp = numlist[i]
    while cnt <= temp:
        numstack.append(cnt)
        opstack.append("+")
        cnt +=1
    
    if numstack[-1] == temp:
        numstack.pop()
        opstack.append("-")
        
    else:
        print("NO")
        flag = False
        break
        
if flag:
    print(*opstack, sep="\n")