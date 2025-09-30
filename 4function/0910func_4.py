print('1=====================================')

# 다양한 매개변수
   # 기본 매개변수 default parameter


# def myAdd(num1, num2, num3=0) :    #default 매개변수는 중간에 입력할 수 없음. 무조건 마지막 파라미터에서 default parameter로 지정 가능함.
#     return num1 + num2 + num3

# def myAdd(num1, num2=0, num3=0) :    #마지막 num3 default parameter로 했으므로, num2 도 default parameter로 지정가능. 
#     return num1 + num2 + num3
#현업에서 파라미터 첫번째 빼고 나머지 default 파라미터로 지정 많이 해놓음.

def myAdd(num1=0, num2=0, num3=0) :    #전부 default parameter로 지정 가능함.
    return num1 + num2 + num3

result1 = myAdd()
result2 = myAdd(1)
result3 = myAdd(1,2)
result4 = myAdd(1,2,3)
print (result1, result2, result3, result4 )
