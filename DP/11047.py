import sys
r = sys.stdin.readline

N, K = map(int, r().rstrip().split())
coins = [int(r()) for _ in range(N)]

cnt = 0

for i in reversed(range(N)):
    cnt += K // coins[i]
    K %= coins[i]
    
print(cnt)