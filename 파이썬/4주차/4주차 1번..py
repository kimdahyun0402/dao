list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #정수의 list를 생성했고 리스트의 이름을 list로 했다
print(list)             
a=int(input("변경할 위치(0~9):")) #변경할 위치를 변수a로 설정하고 숫자로 전환시켰다
b=int(input("새로운 값:"))       #변경할 값을 b라는 변수로 설정하고 숫자로 전환시켰다
list[a]=b                       #리스트의 a위치에 있는 값을 b로 변경시킴
print(list)  
c=int(input("추가할 값:"))    #리스트에 추가할 값을 변수 c로 놓고 숫자로 전환
list.append(c)                #리스트에 c 추가
print(list)
