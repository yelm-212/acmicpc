import sys
r = sys.stdin.readline

N = int(r())
value = [list(map(int, r().rstrip().split())) for _ in range(N)]

for i in range(1, N):
    value[i][0] = min(value[i-1][1], value[i-1][2]) + value[i][0]
    value[i][1] = min(value[i-1][2], value[i-1][0]) + value[i][1]
    value[i][2] = min(value[i-1][1], value[i-1][0]) + value[i][2]
    
print(min(value[N-1]))