import sys
read = sys.stdin.readline

N = int(input())
lenList = list(map(int, read().rstrip().split()))
priceList = list(map(int, read().rstrip().split()))

res = 0
listMin = min(priceList[:-1])

for i in range(len(priceList)):
  if priceList[i] > listMin: 
    # 최소값은 제일 마지막 도시 빼고 고려
    # 최소값이 아니니까 다음 도시 갈때까지 필요한 최소한의 기름만 넣음
    res += priceList[i]*lenList[i]
  else:
    # 최소값일경우 그 도시에서 다 넣고 간다
    res += priceList[i]*sum(lenList[i:])
    break # 이후에 나오는 도시에 대해서도 계산을 마쳤으므로 반복문 나가야함

print(res)