N = int(input())
line = 0; M = 0;

while(N>M):
    line +=1
    M += line #계차수열

tmp = M - N
if (line%2) == 0 : #짝수번째 line
    i = line - tmp
    j = tmp +1
else: #홀수번째 line
    i = tmp +1
    j = line - tmp
    
print(str(i)+"/"+str(j))