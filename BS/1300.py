N = int(input())
k = int(input())

Start, End = 1, k
while Start <= End:
    Mid = (Start + End) // 2
    cnt = 0

    for i in range(1, N+1):
        cnt += min(Mid // i, N)

    if cnt < k:
        Start = Mid + 1
    else:
        res = Mid
        End = Mid - 1

print(res)