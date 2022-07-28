#9012 괄호

import sys
r = sys.stdin.readline

N = int(r())

for _ in range(N):
    stack = []
    temp = r().strip()
    for char in temp:
        if char == "(": 
            stack.append(char)
        elif char == ")": 
            if not stack: 
                print("NO")
                break # 빈 스택
            else:
                stack.pop()
    else:
        if stack : 
            print("NO")
        else:
            print("YES")
    
