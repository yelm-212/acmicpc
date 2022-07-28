import sys
r = sys.stdin.readline
N = int(r())
line = []
for i in range(N):
    line.append(list(map(int, r().split())))
    
# print(*line)

for i in range(N):
    temp = 1
    for j in range(N):
        if line[i][0] < line[j][0] and line[i][1] < line[j][1]:
            temp += 1
    print(temp, end = " ")
    