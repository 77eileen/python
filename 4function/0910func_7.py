# 함수
# 함수명 add
# 파라미터 2개 op1, op2
# 결과를 반환한다.

print('1=====================================')

# 생성
def add (op1, op2):
    result = op1 + op2
    return result

# 사용
print (add (10,20))             #그냥 출력
two_number_hab =add(10,30)      #변수로 만들기
numbers = [ add(10,20), add(1,2), add(4,5)]    #리스트에 만들기
print(numbers)

# 매개변수 받아서 출력하는 함수
# 함수명 : show_number
# 매개변수명 : data

def show_number(data):
    print (f'numbers={data}')

show_number(add(10,2))

print('2=====================================')


#실습1 : 
def count_str(str):
    return len(str)

print(f'count_str 함수 결과 : {count_str('안녕')}')