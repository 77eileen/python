# 간단한 함수
#    함수내의 로직인 한줄로 표현 가능한 함수들
def my_add(a,b):
    return a+b
a,b=10,20
print(f'{a}+{b}={my_add(a,b)}')

# 람다 함수 - 한줄로 표현한 함수     lambda 키워드 사용
# 간단한 함수를 즉석에서 만들 때 유용
# 무조건 값을 리턴하는 함수로, return 키워드 사용 안함
test = lambda c,d : c+d       

c,d=11,22
print(f'{c}+{d}={test(c,d)}')
