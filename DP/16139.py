import sys
read = sys.stdin.readline

string = input()
q = int(input())

#2D array - 각 알파벳에 대한 구간합 미리 계산해 list로 저장하는 방식으로 변경(예정)
def calc(S):
    tmp = list(map(str, read().rstrip().split()))
    a, l, r = tmp[0], int(tmp[1]), int(tmp[2])
    s = 0
    sumlist = [0]
    
    for idx in range(len(S)):
        if  S[idx] == a:
            s += 1
        sumlist.append(s)
        
    return ( sumlist[r+1] - sumlist[l] )

for _ in range(q):
    print(calc(string))
            