from copy import deepcopy
import copy

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def dist(p1, p2):
    d1 = p1.x - p2.x
    d2 = p1.y - p2.y
    return ((d1 * d1) + (d2 * d2))
        
def closest(pt, n):
    p1 = copy.deepcopy(pt)
    p1.sort(key = lambda point: point.x)
    p2 = copy.deepcopy(pt)
    p2.sort(key = lambda point: point.y)
    
    return p2
    
file = open("input.txt", 'r')
n = int(file.readline())

ptlist = []

for i in range (n):
    line = file.readline()
    a, b = map(int, line.split())  
    ptlist.append(point(a,b))
    
newlist = closest(ptlist, len(ptlist))
    
# 확인용
for j in range (n):
    print(newlist[j].x, newlist[j].y)