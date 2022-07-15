n, x = map(int, input().split())
intlist = list(map(int, input().split()))

for num in intlist:
    if num < x:
        print(num, end = " ")