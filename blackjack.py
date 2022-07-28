import sys

N, M = map(int, sys.stdin.readline().split())
list = list(map(int, sys.stdin.readline().split()))
sumlist = []
# print(list)

for i in range(N):
    for j in range(i+1,N):
        for k in  range(j+1,N):
            sum = list[i] + list[j] + list[k]
            if sum<=M: 
                sumlist.append(sum)

res= max(sumlist)
print(res)