import sys
r = sys.stdin.readline # 더 빠른 파일 입출력
        
x,y,w,h = map(int, r().split())  

print(min(x,y,w-x,h-y))