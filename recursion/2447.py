N = int(input())
default = ["***", "* *", "***"]

def recprint(divend):
    if (divend == 3):
        return default

    qutlist = recprint(divend // 3) # N/3 list 반환
    newlist = []
    for i in qutlist:
        newlist.append(i*3)
    for i in qutlist:
        newlist.append(i*3)
        
    # for i in range(0,N,qut):
    #     pass
    
lists = []
recprint(N)
print(*lists, sep="")