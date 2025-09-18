print('1=====================================')
import random
print (random.randint(1,5))  #=> () 괄호 형태를 가지고 있으면 "함수" / 함수 중 값을 반환하는 애들도 있고, 안하는 애들도 있음. 정해진건 없음.
result = print('hi')        
print(result)                #=> print는 반환하지 않는 함수. result = print() print는 없는데 받는것으로 프로그래밍 되어 있어서 none으로 나옴.
print('2=====================================')
# 함수 정의 def 키워드 사용
# 매개변수(Parameter) : 함수가 전달받는 값
# 인자(Argument)      : 함수를 호출할 때 전달하는 값   ref. 현업에서는 매개변수, 인자 모두 파라미터라고 사용함.
# 반환값(Return Value) : 함수가 작업을 마치고 호출한 곳으로 돌려주는 값.
#   return 키워드 사용

# 함수의 구성요소
# 4. 매개변수와 반환값이 모두 있는 함수
def myCalc(num1, num2):
    '''                                 #==> 필수는 아니지만, def 정의함수이므로 영어로 설명해놓음. 그럼 해당함수에 마우스 올려두면 설명 팝업으로 나옴
    # 두 개의 값을 받아서 더하는 기능   
      -num1는 숫자
      -num2는 숫자
    '''                                
    result = num1 + num2
    return result                 #=> return은 필수가 아님. return 없이 print(return 없이 콘솔에 바로 출력하는 함수)로 해도 됨. 

#1. 매개변수와 반환값이 없는 함수
def say_hello():
    print('안녕하세요')

say_hello()

#2. 매개변수가 있고 반환값이 없는 함수
def say_hello_name(name):
    print(f'{name}님 안녕하세요')

say_hello_name('홍길동')

#3. 매개변수가 없고, 반환값이 있는 함수
import datetime
def get_current_time():
    return datetime.datetime.now()

print(get_current_time())

#def 함수 만드는 이유
#1. 없는 함수를 만들어서 계속 그 함수를 재활용하기
#2. 소스코드가 길어질 때 수정과 분석을 용이하게 해서 가독성을 높일 수 있음.
#   목차처럼 함수를 정의해놓으면 나중에 수정/확인 시 해당 함수로 바로 찾아서 용이.
# myCalc 호출
myCalc(10) #==> 오류발생 내용 확인해보기. num1, num2로 정의했는데 num2 입력이 안되었다. 