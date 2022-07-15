n = int(input())

a, a_d = n//3, n % 3
b, b_d = n//5, n % 5
for i in range(a):
    new = (n - 3*i)
    b_new = new //5 
    b_d_new = new % 5
    if b_d_new == 0:
        res3 = i+b_new
        break
    else:
        res3= -1
            
if a_d == 0 :
    if not res3 == -1:
        print(min(a,res3))
    else: print(a)
elif b_d == 0 :
    if not res3 == -1:
        print(min(b,res3))
    else: print(b)
else:
    print(res3)
        
        
    