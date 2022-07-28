N = int(input())

for i in range(N):
    temp = i + sum(map(int, str(i)))
    if temp == N:
        M = i 
        break
    else:
        M = 0
    
print(M)