list = [int(input()) for _ in range(9)]
print(max(list))
print(list.index(max(list))+1)

o = 0
x = 0
str = input()
for i in str:
    if (i =="O"):
        o +=1
    elif (i =="X"):
        x +=1
    print()
    