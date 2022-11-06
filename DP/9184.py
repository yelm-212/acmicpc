#    신나는 함수 실행 #9184

import sys
r = sys.stdin.readline

visited = [[[0]*21 for _ in range(21)]for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    if visited[a][b][c]: 
        return visited[a][b][c]
    
    if a < b and b < c:
        visited[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return visited[a][b][c]
    
    else:
        visited[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return visited[a][b][c]
    

while True:
    A, B, C = map(int, r().rstrip().split())
    if A == -1 and B == -1 and C == -1: # 출력 종료
        break
    
    ret = w(A, B, C)
    print( "w({}, {}, {}) = {}".format(A,B,C, ret))