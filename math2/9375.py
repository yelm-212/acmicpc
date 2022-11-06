import sys
r = sys.stdin.readline

def calculate(dic):
    if len(dic.keys()) == 0:
        return 0
    elif len(dic.keys()) == 1:
        vallist = list(dic.values())
        result = 1
        for value in vallist:
            result *= len(value)  
        return result
    else:
        vallist = list(dic.values())
        result = 1
        for value in vallist:
            result *= (len(value) +1) 
        return result -1 # 아무것도 X인 경우 삭제

T = int(r())

for _ in range(T):
    newdict = {}
    N = int(r())

    for i in range(N):
        value, key = map(str, r().rstrip().split())
        if key in newdict:
            newdict[key].append(value)
        else:
            newdict[key] = [value]
    
    print(calculate(newdict))