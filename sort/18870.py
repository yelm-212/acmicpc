import sys
r = sys.stdin.readline

N = int(r())
inputlist = list(map(int,r().split()))
inputslist = sorted(list(set(inputlist)))

dic = {inputslist[i]:i for i in range(len(inputslist))}

for point in inputlist: print(dic[point], end = " ")