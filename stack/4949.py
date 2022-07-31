#4949 

import sys
r = sys.stdin.readline

while True:
    temp = r().rstrip()
    
    stack = []
    flag = True
    
    for char in temp:
        if char == "(" or char =="[": 
            stack.append(char)
        elif stack and (char == ")" or char =="]"): 
            if char == ")" and stack[-1] == "(": 
                stack.pop()
            elif char =="]" and stack[-1] == "[": 
                stack.pop()
            else:
                flag = False
        elif not stack and (char == ")" or char =="]"): 
            flag= False
    
    if temp == ".": break

    if flag and not stack : 
        print("yes")
    else:
        print("no")
    
