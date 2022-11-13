import heapq
import sys

r = sys.stdin.readline

heap1 = []
heap2 = []
N = int(input())

for _ in range(N):
    x = int(r().rstrip())
    if len(heap1) == len(heap2):
        heapq.heappush(heap1, -x)
    else:
        heapq.heappush(heap2, x)

    if heap1 and -heap1[0] > heap2[0]:
        maxval= heapq.heappop(heap1)
        minval = heapq.heappop(heap2)

        heapq.heappush(maxval, -minval)
        heapq.heappush(minval, -maxval)

    print(-heap1[0])