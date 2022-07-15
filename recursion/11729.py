def hanoi(A, B, C, n): 
    if n == 1:
        print(A,C)
    else:
        hanoi(A,C,B,n-1)
        print(A,C)
        hanoi(B,A,C,n-1)
        
N = int(input())
print(2**N-1)
hanoi(1,2,3,N)