import math
print("ax^2+bx+c=0에 대한 해를 구하는 프로그램입니다.") 
a=int(input("a의 값:"))  #a의 값을 정수로 바꾼다
b=int(input("b의 값:"))   #b의 값을 정수로 바꾼다
c=int(input("c의 값:"))   #c의 값을 정수로 바꾼다
x1=(-b + math.sqrt(b*b-4*a*c))/(2*a) #근의 공식에서 나오는 첫번째 x값을 구함
x2=(-b - math.sqrt(b*b-4*a*c))/(2*a) #두번째 값을 구하는 식

print(str(a)+ "x^2+"+str(b)+ "x+"+ str(c)+"=0 의 해는"+str(x1),str(x2) )
