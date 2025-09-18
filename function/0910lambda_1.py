# # 람다가 사용되지 않는 상황
# def add(a,b):
#     return a+b

# def minus(a,b):
#     return a-b

def calc(func, a,b):     #calc 함수를 실행하기 위해 add, minus 함수를 만듬.. 곱하기 나누기도 계속 만들어야함 => 이럴때 lambda!
    return func(a,b)

#print (calc(add,1,2))     #calc 호출 -> add 함수 호출 -> return 값이 calc로 들어옴 -> print로 호출


# 람다 사용
print (calc(lambda a,b : a+b, 1,2))      #람다 함수는 임시/간단히 쓰고 버림. 상기는 add, minus 함수가 계속 살아있음. 
print (calc(lambda x,y : x*y, 10,20))
