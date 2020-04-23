list=[]                    
a= int(input("정수 1 :"))  #리스트에 들어갈 정수를 a라는 변수로 놓음
b= int(input("정수 2 :"))
c= int(input("정수 3 :"))
d= int(input("정수 4 :"))
list.append(a)             # 위에서 받은 정수를 차례로 리스트에 추가
list.append(b)    
list.append(c)
list.append(d)

print(list)

print("평균: %5.2f"%((a+b+c+d)/4))   # 리스트에 있는 4개 정수의 평균을 계산함
                        #문자열 삽입 연산자 %를 이용해 소수점 2자리까지 출력
            
