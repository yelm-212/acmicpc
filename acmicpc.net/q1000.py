a , b= map(int, input().split())
print(a+b , a-b, a*b, a//b , a%b, sep='\n') 

a , b= map(int, input().split())
print(a+b) # python에서는 자기가 알아서 typecast되어 출력됨! float로 받을 필요 없음
print(a-b)
print(a*b)
print(a//b)
print(a%b)
