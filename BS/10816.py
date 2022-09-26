import sys

r = sys.stdin.readline

N = int(r())
sack = list(map(int, r().split()))
sack.sort()

M = int(r())
check = list(map(int, r().split()))

dic = {}
for card in sack:
    if card in dic: dic[card] += 1
    else: dic[card] = 1


def find(L: list, target: int, S: int, E: int):
    if S > E:
        return 0
    mid = (S + E) // 2
    if L[mid] == target:
        return dic.get(target)
    elif L[mid] > target:  #왼쪽
        return find(L, target, S, mid - 1)
    else:  # 오른쪽
        return find(L, target, mid + 1, E)


for checklist in check:
    print(find(sack, checklist, 0, len(sack) - 1), end=" ")
