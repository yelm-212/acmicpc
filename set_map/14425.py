import sys
r = sys.stdin.readline
cnt = 0

N, M= map(int, r().split()) 

setlist = set([r() for _ in range(N)])
checklist = [r() for _ in range(M)]


for string in checklist:
    if string in setlist : 
        cnt +=1
    else: 
        pass
    
print(cnt)