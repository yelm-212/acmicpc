n = int(input())
rem = n % 5
bag3=0

if rem == 0 :
    print(n // 5)
elif n<3:
    print(-1)
else:
    while True:
        n = n-3
        bag3 +=1
        rem = n % 5
        if rem == 0 :
            bag3 += n // 5
            print(bag3)
            break
        elif n == 0:
            print(bag3)
            break
        else :
            print(-1)
            break
        
        