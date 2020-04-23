a=int(input("첫번째 정수를 입력하세요:")) # 각각의 정수를 받는다.
b=int(input("두번째 정수를 입력하세요:"))
c=int(input("세번째 정수를 입력하세요:"))

d=a-b               #a-b 값을 d로 설정한다.양수인지 음수인지 판단하기 간단하다. 
e=a-c
f=b-c

if d>0:          #a가 b보다 큰 경우 나올 수 있는 경우의 수는 3가지이다.
    if e>0:     #a가 b보다 크고 a가 c보다 큰 경우 f값을 확인해야한다.
        if f>0:   # b가 c보다 큰 경우
            print("순서대로 정렬한 결과: %d,%d,%d"%(c,b,a))
        else :   # b가 c보다 작은 경우
            print("순서대로 정렬한 결과: %d,%d,%d"%(b,c,a))
    else:       #a가 b보단 크지만 c보다 작은 경우
         print("순서대로 정렬한 결과: %d,%d,%d"%(b,a,c))
else:            #a가 b보다 작은경우
    if f>0:
        if e>0:
            print("순서대로 정렬한 결과: %d,%d,%d"%(c,a,b))
        else :
            print("순서대로 정렬한 결과: %d,%d,%d"%(a,c,b))
    else :
        print("순서대로 정렬한 결과: %d,%d,%d"%(a,b,c))
