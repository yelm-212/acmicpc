import sys
from math import sqrt
 
inf = 123456789

r = sys.stdin.readline
N = int(r())
# n개의 입력을 2D array로 받아들인다.

DP = [[-1 for _ in range(1<<N)] for _ in range(N)]
distance = [[0 for _ in range(N)] for _ in range(N)]

points = []
for i in range(N):
    points.append(list(map(float, r().split())))

def dist(a1,a2):
    return sqrt((a1[0] - a2[0])**2 + (a1[1] - a2[1])**2)
# 비용은 list 내의 좌표평면 위 점p1, p2에 대해 두 점 사이의 거리로 계산한다.
 
def tsp(now, visited):
    # 재귀호출을 통해 구현
    # now : 현재 도시, v: 방문한 도시
    if visited == (1<<N)-1:
        if distance[now][0]: 
            return distance[now][0]
        return inf
    
    if DP[now][visited] != -1: 
        return DP[now][visited]
 
    DP[now][visited] = inf
    for i in range(N):
        if not visited&(1<<i) and distance[now][i]:
            # DP[now][visited] = min(DP[now][visited],tsp(i, visited|(1<<i)) + distance[now][i])
            if DP[now][visited] >= tsp(i, visited|(1<<i)) + distance[now][i] :
                DP[now][visited] = tsp(i, visited|(1<<i)) + distance[now][i]
#                select[now][visited] = i
    
    return DP[now][visited]
        
for i in range(N):
    for j in range(N):
        if i==j: continue
        distance[i][j] = dist(points[i], points[j])
# distance list를 통해 TSP()내에서 접근이 가능하도록 한다.
 
print(tsp(0,1))
