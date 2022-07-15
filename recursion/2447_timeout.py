def recprint(x, y, divend):
    if (divend == 3):
        list[1+x][1+y] = " "
        return 
    else:
        qut = divend // 3 # N/3 
        for i in range(x+qut, x+2*qut):
            for j in range(y+qut, y+2*qut):
                list[i][j] = " "
        for i in range(0,N,qut):
            for j in range(0,N,qut):
                if ((x+i) < N) and ((y+j) <N):
                    recprint(x+i, y+j,qut)
    
N = int(input())
list = [["*" for _ in range(N)] for _ in range(N)]
recprint(0,0,N)
for i in range(N):
    print(*list[i], sep="")