import sys
read = sys.stdin.readline

N = int(input())
lenList = list(map(int, read().rstrip().split()))
priceList = list(map(int, read().rstrip().split()))

priceList.pop()
# 가격은 제일 마지막 도시 빼고 고려해도 동일함

res = 0
listMin = priceList[0]

for i in range(len(priceList)):
  if priceList[i] < listMin: 
    listMin = priceList[i]
    # min() 쓰지 않고각 도시에서 최소비용 계산 -> 선택 정렬과 유사한 과정
  res += listMin *lenList[i]

print(res)