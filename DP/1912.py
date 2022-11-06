import sys
r = sys.stdin.readline

N = int(r())
nlist = list(map(int, r().rstrip().split()))

for i in range(1, N):
    nlist[i] = max(nlist[i], nlist[i-1]+ nlist[i])
# for 문을 돌면서 이잔까지의 합의 값과 현재 값 중 큰 값으로 갱신해 저장한다.
    
print(max(nlist))