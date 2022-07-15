def fibo(k): 
    if (k == 0): return 0
    elif (k == 1): return 1
    else:
        return (fibo(k-1) + fibo(k-2))

N = int(input())

print(fibo(N))

