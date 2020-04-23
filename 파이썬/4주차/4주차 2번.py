list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)
a=int(input("변경할 위치(0~9): "))
b=int(input("새로운 값: "))
list[a]=b
print(list)
c=int(input("추가할 값: "))
list.append(c)
print(list)
