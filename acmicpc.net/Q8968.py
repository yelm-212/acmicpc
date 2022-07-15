n = int(input())
for _ in range (n):
    a = list(input())
    point = 0
    sumpoint = 0
    for i in a:
        if i == "O":
            point  +=1
        else:
            point = 0
        sumpoint += point
    print(sumpoint)