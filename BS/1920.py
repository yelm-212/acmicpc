import sys
# 그냥 set 만들어 문제 풀어도 무방함
# (시간 복잡도 동일함)
r = sys.stdin.readline

N = int(input())
nlist = list(map(int, r().rstrip().split()))

M = int(input())
mlist = list(map(int, r().rstrip().split()))

dict = {}

for i in nlist:
    if i in dict:  # 이미 있음
        pass
    else:
        dict[i] = 1

for i in mlist:
    if i in dict:
        print(dict[i])
    else:
        print(0)
