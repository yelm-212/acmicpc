import sys
r = sys.stdin.readline

A, B = map(int, input().rstrip().split())
x, y = A, B

while y:
    x, y = y, x % y
    
print(x)
print(A*B // x)

# 유클리드 호제법 - https://wikidocs.net/21759