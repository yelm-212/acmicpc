from collections import deque
import sys
r = sys.stdin.readline
T = int(r())

for _ in range(T):
    plist = r().rstrip()
    n = int(r().rstrip())
    temp = r().rstrip()[1:-1]
    
    flag = True
    reverseflag = False
    
    if n == 0: 
        intlist = deque()
    else:
        intlist = deque(map(int, temp.split(',')))
        
    
    for command in plist:
        if command == 'R':
            reverseflag = not reverseflag
        else:
            if intlist and command == 'D':
                if reverseflag:             # reverseflag가 true - reverse 시행 예정
                    intlist.pop()           # 오른쪽에서 pop해준 뒤 나중에 reverse해줄것임
                else:
                    intlist.popleft() 
            else:
                flag = False
                break
            
    if reverseflag : intlist.reverse()
        
    if flag:
        print("[", end = "")
        print(*intlist, sep = ",", end = "")
        print("]")
    else: 
        print("error")
            