import heapq
import sys

r = sys.stdin.readline

heap = []
N = int(input())

for _ in range(N):
    x = int(r().rstrip())
    if x:
        heapq.heappush(heap, (-x, x))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])

