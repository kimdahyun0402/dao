a=int(input("100미만 양의 정수 복권번호를 입력하세요:")) #복권번호 입력받음

import random   
computer_choice = random.randint(1,100) #당첨번호를 랜덤으로 설정한다.
b= computer_choice           #당첨번호를 b로 놓는다
user_choice = a

print("당첨번호는 %d입니다!"%(b)) 

if a==b :               #당첨번호와 복권번호가 같을경우 상금 100만
    print("상금: 100만원")

elif ((a//10 == b//10) or (a%10 == b%10)): #같은자리에 같은값이 있을 경우 20만원
    print("상금: 20만원")
elif ((a//10 == b%10) and (a%10 == b//10)): 
    print("상금: 10만원")  #같은자리는 아니지만 숫자가 두개다  같을경우 10만원
elif ((a//10 == b%10) or (a%10 == b//10)):   
    print("상금: 5만원")   #같은자리는 아니지만 숫자가 하나만 같을 경우 5만원

else :                  #모두 아닌경우 상금이 없다.
    print("상금은 없습니다")

    
