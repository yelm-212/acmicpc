import sys

read = sys.stdin.readline

N = int(input())
times = []

for _ in range(N):
    temp = list(map(int, read().rstrip().split()))
    times.append(temp)

for i in range(N):
  lenTmp = times[i][1] - times[i][0]
  times[i].append(lenTmp)

times.sort(key=lambda x: (x[1], x[0], x[2]))
endTmp = times[0][1]
res = 1

for i in range(1, N):
    startTmp = times[i][0]
    if startTmp >= endTmp:
        res += 1
        endTmp = times[i][1]
    else:  # startTmp < endTmp
        continue

print(res)
