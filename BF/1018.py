import sys
r = sys.stdin.readline
N, M = map(int, r().split())

checkerboard = [r() for _ in range(N)]
checkerboardcnts = []
for i in range(N-7):
    for j in range(M-7):
        temp1 = 0
        temp2 = 0
        
        for y in range(i, i+8):
            for x in range(j, j+8):
                if (x+y)%2:
                    if checkerboard[y][x] != "W": temp1 +=1
                    if checkerboard[y][x] != "B": temp2 +=1
                else:
                    if checkerboard[y][x] != "W": temp2 +=1
                    if checkerboard[y][x] != "B": temp1 +=1
                    
        checkerboardcnts.append(min(temp1, temp2))
                    
print(min(checkerboardcnts))

            
    # for char in checkerboard[i]:
        # print(char, end ="")
        # char = temp
        # if temp != char and temp != "":
        #     checkerboardcnt[i] -=1

