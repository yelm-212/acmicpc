lines = input().rstrip()

lineM = list(lines.split("-"))
res = 0

for i in range(len(lineM)):
  tempVal = sum(list(map(int, lineM[i].split("+"))))
  if i == 0:
    res += tempVal
  else:
    res -= tempVal

print(res)
  