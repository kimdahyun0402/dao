x1=float(input("첫 번째 점의 x좌표:")) #점의 좌표들을 부동소수점으로 입력받는다.
y1=float(input("첫 번째 점의 y좌표:")) 
x2=float(input("두 번째 점의 x좌표:"))
y2=float(input("두 번째 점의 y좌표:"))

import turtle           
t=turtle.Turtle()
import math       #(x1,y1)점과 (x2,y2)점 사이의 거리 공식을 이용한다.  
t.write("점의 길이="+ "%.3f" %(math.sqrt((x1-x2)**2+(y1-y2)**2)))#소수점 자리 설정
t.up()
t.goto(x1,y1)
t.down()
t.write("({},{})".format(x1,y1))  #점의 좌표를 나타낸다. 가로를 포함시킨다.

t.goto(x2,y2)                #(x2,y2) 좌표로 이동
t.write("({},{})".format(x2,y2))

t.up()            #커서를 원점으로 이동시키기 위해 띄운다.
t.goto(0,0)        #원점으로 커서를 이동시킨다.
 
