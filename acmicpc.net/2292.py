# 1, 7 ,19, 37
#  6 , 12, 18
# 1, 2, 8, 20, 38
#   1, 6, 12, 18

a = int(input())
n = 1
cnt = 1

while(a>n):
    n += 6*cnt
    cnt += 1
print(cnt)
    
H, M = map(int, input().split())    
if M>=45:
    print(H, M-45)
elif H>0:
    print(H-1, M+15)
else: # 0시인 경우
    print(23, M+15)
    


