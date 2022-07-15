n = int(input())
n_new = n
cnt =0

while True:
    tmp1 = n_new//10
    tmp2 = n_new%10
    tmp3 = (tmp1+tmp2)%10
    n_new = tmp2*10 + tmp3
    cnt+=1
    if (n_new == n):
        break
    
print(cnt)
import sys
N = sys.stdin.readline()
lines = sys.stdin.readlines()
for line in lines:
    a, b = map(int, line.split())
    print(a+b)
    
