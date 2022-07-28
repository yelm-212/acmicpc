N = int(input())

n1 = 0
n2 = 1
# temp = 0

if N <=1: print(N)
else:
    for i in range(2,N+1):
        temp = n2
        n2 = n2 + n1 # n2 값 갱신
        n1 = temp # 기존 n2값을 n1으로 바꿈
    print(n2)