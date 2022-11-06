while True:
    A, B = map(int, input().rstrip().split())
    
    if A == 0 and B == 0: # 종료조건
        break
    
    if A < B:
        if B % A: 
            print("neither")
        else: 
            print("factor")
    else:
        if A % B: 
            print("neither")
        else: 
            print("multiple")
        