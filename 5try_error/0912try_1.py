#구문오류 (SyntaxError) : 오타 / 실행하기전에 발생된 것. / 문법이 미완성된 것
#예외 (exception) : 런타임 오류 / 실행하고나서 문법 오류 발생

print ("==========오류 예시 1=============")
#예외 상황 확인하기
#ex. 예외가 발생할 수 있는 코드
# number_input_a = int(input('정수 입력'))

# print("원의 반지름:", number_input_a)
# print("원의 둘레", 2*3.14*number_input_a)
# print("원의 넓이", 3.14*number_input_a*number_input_a)
#===> 발생가능 오류: 한글로 숫자 입력, 좌우 공백 ( .stream? 좌우공백 제거), 소수점 기재
#  .isdigit()  ==> 숫자로만 이루어졌는지 판단하는 매서드
print(int(12.3))    #결과 12   : 오류는 발생되지 않지만 12.3 원하는 값으로 인지되지 않음.
print(float(12.3))  #결과 12.3


print ("==========오류 예시 2 예외처리=============")
#오류를 피해가는 행위 ==> 예외처리
try: 
    num1, num2 = map (int, input ('공백을 기준으로 두개의 숫자를 입력: ').split())

    calc_lists=[num1+num2, num1+num2, num1*num2, num1/num2]

    print ('1. 더하기', end='\t')  #\t 탭키를 입력하는 것
    print ('2. 빼기', end='\t\t')
    print ('3. 곱하기', end='\t')
    print ('4. 나누기', end='\t')
    choice = int(input ('원하는 결과를 입력하세요'))   
    print(f'결과는 = {calc_lists[choice]}')
        #choice 4로 하는 경우, calc_lists 에 인덱스[4]의 값이 없으므로 오류 발생.
        #해결 : print(f'결과는 = {calc_lists[choice]}') ===> print(f'결과는 = {calc_lists[choice-1]}')

except: #오류발생되면 except
    #pass    #오류 발생되면 except - pass - print('프로그램 종료') ==> 무슨 오류인지 알수 없음
    print('오류발생')  # ==> 무슨 오류인지 알수 없음.

print("프로그램 종료")




#======= 발생 가능성 에러
#IndexError: list index out of range
    #choice 4로 하는 경우, calc_lists 에 인덱스[4]의 값이 없으므로 오류 발생.
    #해결 : print(f'결과는 = {calc_lists[choice]}') ===> print(f'결과는 = {calc_lists[choice-1]}')
#ValueError: invalid literal for int() with base 10: '백' 
    #값을 input으로 int 로 바꿀수 없는 경우 (문자 입력)
#ZeroDivisionError: division by zero 
    #값을 input으로 0을 입력하는 경우.
#원하는 결과 값으로 더하기, 빼기 한글로 작성한 경우.


#========= try except else finally 구문==================================
#try except 구문 : 예외를 처리할 수 있는 구문
#try : 
    #예외가 발생할 가능성이 있는 코드
#except:
    #예외가 발생했을 때 실행할 코드
#else:
    #예외가 발생하지 않았을 때 실행할 코드 (try구문에서 return이 있으면 else로 작동안함.)
    #else ===> 현업에서 잘 사용안함.
#finally:
    #무조건 실행할 코드 (try구문내에서 return이 있어도 무조건 실행)
    #finally ===> 현업에서 잘 사용안함.  ==> with절?? 을 더 많이 사용함.



#========= 예외 객체 (exception object)==================================
#try except 구문 : 예외를 처리할 수 있는 구문
#try : 
    #예외가 발생할 가능성이 있는 코드
#except 예외의 종류 as 예외 객체를 활용할 변수 이름(별칭 할당):
    #예외가 발생했을 때 실행할 코드
    #Exception : 모든 예외의 어머니 (valueError 등 모든것의 상위 class)
    #Exception as exception ==> 실무에서는 Exception as e 로 작성함