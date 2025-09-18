print('1=====================================')

# 다양한 매개변수
   # 기본 매개변수 default parameter

def myAdd(num1, num2=0) :    #num1 = positional 매개변수 #num2는 default 매개변수
    return num1 + num2

result = myAdd(10,20)        #매개변수 2개 입력하므로 기본 매개변수 작동안함.
print(f'매개변수 2개 기재 : result = {result}')

result = myAdd(10)           #매개변수 num2=0 default 값이 주어졌기 때문에, 사용자가 num2를 입력하지 않아도 0이 기재된것으로 인식해서 오류 안생김.
print(f'매개변수 1개 기재, default매개변수 작동 : result = {result}')