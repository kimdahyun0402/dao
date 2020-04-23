import time           
fseconds = time.time()  #time.time() 함수를 사용
total_sec = int(fseconds)  #초를 정수로 바꾼다
total_min = total_sec // 60   #지금까지 지나온 분
total_hour = total_sec//3600  #지금까지 지나온 시간
min= int(total_min%60)   #지금의 min은 total min에서 60을 나눈 나머지이다.
hour=int((total_hour%24+9)%12) #지금 시간은 total_hour을 24로 나눈 나머지에
             #한국 표준시간을 위해 +9를 해주고 문제 조건처럼
             #13시일 경우 1시로 나타내기 위해 12로 나눈 나머지가 현재 시간이다.
print("지금은 한국 표준시간으로",hour,"시",min,"분입니다")
