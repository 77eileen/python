#========= 예외 객체 (exception object)==================================
#try except 구문 : 예외를 처리할 수 있는 구문
#try : 
    #예외가 발생할 가능성이 있는 코드
#except 예외의 종류 as 예외 객체를 활용할 변수 이름(별칭 할당):
    #예외가 발생했을 때 실행할 코드
    #Exception : 모든 예외의 어머니 (valueError 등 모든것의 상위 class)
    #Exception as exception ==> 실무에서는 Exception as e 로 작성함


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

except ValueError as e:
    print(f'오류발생, 숫자를 입력하세요 : {e}')
except IndexError as e:
    print(f'오류발생, 개발자에게 문의 : {e}')
except Exception as e:
    print(f'그밖의 에러  : {e.__class__.__name__ } \n 설명: {e}')
    # e.__class__.__name__ : class 이름을 알수있음. (정확한 error  이름 확인 가능)

    #실제 발생 오류 이름
        #IndexError: list index out of range
        #ValueError: invalid literal for int() with base 10: '백' 
        #ZeroDivisionError: division by zero 
    #Exception 대신 상기와 같은 IndexError , ValueErro, ZeroDivisionError 등과 같은 상세한 오류를 기재해서 특정 에러에 대해 설계가능.
    #===> but, 현업에서 90% 이상이 모두 Exception 을 사용함.

print("프로그램 종료")





