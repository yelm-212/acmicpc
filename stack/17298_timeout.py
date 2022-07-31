import sys
r = sys.stdin.readline

N = int(r())

stack = list(map(int, r().split()))

for i in range(N):
    if i < (N-1): 
        temp = stack[i:]
        for idx in temp:
            if stack[i] < idx :
                nge = idx
                break
            else: 
                nge = -1
        print(nge, end= " ")
            
    else: print(-1, end=" ")
    
    
    
# 시간 복잡도가 O(N^2)이 되어 timeout이 뜬다.