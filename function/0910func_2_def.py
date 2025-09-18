# 매개변수 O, 반환값 O
# 매개변수 O, 반환값 X
# 매개변수 X, 반환값 O
# 매개변수 X, 반환값 X

# 만들고 사용해보기.
print('1=====================================')
# 매개변수 O, 반환값 O
def gugudan(num1, num2) :
    '''
    구구단 : num1 X num2
    '''
    result = num1 * num2
    return result
print (gugudan (4,5))
# 매개변수 O, 반환값 X
def student (name, age, id):
    '''
    이름, 나이, ID정보를 입력해서 학생 정보를 출력
    '''
    print (f'{name}님 : 나이 {age}, 학번 {id}')
student('홍길동', 20, 5468)
# 매개변수 X, 반환값 O
def lotto ():
    '''
    랜덤한 로또 번호 6자리 호출
    '''
    import random
    lotto_num = random.sample (range(1,45), 6) 
    return lotto_num
print (lotto())
# 매개변수 X, 반환값 X
def thanks ():
    '''
    감사합니다 를 출력합니다.
    '''
    print ('감사합니다.')
thanks()

