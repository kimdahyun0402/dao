x1=float(input("첫 번째 점의 x좌표:"))
y1=float(input("첫 번째 점의 y좌표:"))
x2=float(input("두 번째 점의 x좌표:"))
y2=float(input("두 번째 점의 y좌표:"))

x1*=1000
y1*=1000
x2*=1000
y2*=1000

import math
a=int(math.sqrt((x1-x2)**2+(y1-y2)**2))
a=float(a/1000)
print("두 점 사이의 거리:",a)
