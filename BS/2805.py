import sys

r = sys.stdin.readline

N, M = map(int, r().rstrip().split())
heightList = list(map(int, r().rstrip().split()))

maxHeight = max(heightList)


def check(cut: int) -> bool:
    sum = 0
    for height in heightList:
        if height >= cut:
            tmp = height - cut
            sum += tmp

    if sum >= M:
        return True
    else:
        return False


Start, End = 0, maxHeight

while (Start <= End):
    mid = (Start + End) // 2
    if check(mid):
        Start = mid + 1
    else:
        End = mid - 1

print(End)
