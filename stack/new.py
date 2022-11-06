import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    a = list(input())
    sum = 0
    for i in a:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        elif sum < 0:
            print("NO")
            break
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")