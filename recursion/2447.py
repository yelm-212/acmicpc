import sys
N = int(sys.stdin.readline())

def recprint(divend):
    if (divend == 1):
        return ["*"]
    
    list = [] # 새로운 빈 리스트 선언 (local var.)
    qut = (divend // 3) # N/3 list 반환
    qutlist = recprint(qut)
    for i in qutlist:
        list.append(i*3)
    for i in qutlist:
        list.append(i+' '*qut+i)
    for i in qutlist:
        list.append(i*3)
    return list

# print('\n'.join(recprint(N)))
for i in range(N):
    print(*recprint(N)[i], sep="")
