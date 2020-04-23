print("ax^2 + bx + c=0 에 대한 실수해를 구하는 프로그램입니다.")
a=int(input("a의 값:"))  #a,b,c의 값을 정수로 입력받는다.
b=int(input("b의 값:"))
c=int(input("c의 값:"))

import math

D = b*b - 4*a*c     #이차방정식 해를 판별하기 위한 판별식

if D>0:             #판별식이 0보다 클 경우 이차방정식의 해가 2개이다.
    x1=(-b + math.sqrt(b*b-4*a*c))/(2*a) #x1과 x2의 값을 구한다
    x2=(-b - math.sqrt(b*b-4*a*c))/(2*a)
    print("%dx^2 + %dx + %d = 0 의 실수해는 %f, %f 입니다."%(a,b,c,x1,x2))

elif D==0:        #판별식이 0일 경우 이차방정식은 중근을 가진다.
    x3=(-b + math.sqrt(b*b-4*a*c))/(2*a) #중근을 x3로 설정한다.
    print("%dx^2 + %dx + %d = 0 의 실수해는 %f입니다."%(a,b,c,x3))

else:           #위의 경우가 아닌 나머지 경우는 D<0인 경우이다
                #D<0인 경우 이차방정식의 실수해는 없다.
    print("%dx^2 + %dx + %d = 0 의 실수해는 없습니다."%(a,b,c))






    









      
