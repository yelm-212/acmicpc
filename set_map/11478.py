import sys
r = sys.stdin.readline

string = r().strip()
sets = set()
for i in range(len(string)):
    for j in range(i, len(string)):
        sets.add(string[i: j+1])
        
print(len(sets))