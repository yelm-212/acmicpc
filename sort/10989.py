import sys
r = sys.stdin.readline

def cntsort(arr, max):
    # max = max(arr)
    cntarr = [0]*(max+1) 
    
    for i in arr:
        cntarr[i] +=1

    for i in range(max):
        cntarr[i+1] += cntarr[i]
        
    sorted_arr = [-1] * len(arr)
    
    for i in arr:
        sorted_arr[cntarr[i] - 1] = i
        cntarr[i]-= 1
    
    return sorted_arr

N = int(r())
inputlist =  [int(r()) for _ in range(N)]
sortedlist = cntsort(inputlist, max(inputlist))
print(*sortedlist, sep="\n")