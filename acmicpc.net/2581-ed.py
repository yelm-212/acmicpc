M = int(input())
N = int(input())
list = []

for i in range (M, N+1):
    for j in range (2, i+1):
        if i == j:
            list.append(i)

        if i % j ==0: 
            break

if not list:
    print("-1")
else:
    print(sum(list))
    print(list[0])