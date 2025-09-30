# 논리 연산자 사용
# 나이가 18이상(성인) 이면서 주민번호를 가진 사람은 "입장가능" "입장불가"
has_id = False
age = int (input ('나이를 입력하세요: '))
print (f'입력된 나이는 {age}') 

if age >= 18 and has_id == True:
    print ('입장가능')
elif age <18 or has_id == False:
    print ('입장불가능')
print('종료')