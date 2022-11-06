import sys
r = sys.stdin.readline

N = int(r())
numlist = list(map(int, r().rstrip().split()))
op = list(map(int, r().rstrip().split()))

maximum = -1000000000
minimum = 1000000000

def calc(n, tmpres, add, sub, mult, div):
    global maximum, minimum # 차후 출력을 위함
    if n == N: 
        maximum = max(tmpres, maximum)
        minimum = min(tmpres, minimum)
        return

    if add:
        calc(n+1, tmpres + numlist[n], add-1, sub, mult, div)
    if sub:
        calc(n+1, tmpres - numlist[n], add, sub - 1, mult, div)
    if mult:
        calc(n+1, tmpres * numlist[n], add, sub, mult-1, div)
    if div:
        calc(n+1, int(tmpres / numlist[n]), add, sub, mult, div-1)

calc(1,numlist[0], op[0], op[1],op[2], op[3])

print(maximum)
print(minimum)