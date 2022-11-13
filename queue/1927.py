import heapq
import sys

r = sys.stdin.readline

heap = []
N = int(input())

for _ in range(N):
    x = int(r().rstrip())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print('0')
    else:
        heapq.heappush(heap, x)