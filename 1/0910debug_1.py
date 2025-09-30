#디버그 연습
# for i in range(5) :   #디버깅 단축키 : F10 라인 단위로 실행, F11 은 해당 함수까지 타고 들어감. 
#     print(i)

# print('1=============================')
def say_hello(a):
    return f'{a}님 반갑습니다.'

name='홍길동'
result = say_hello(name)
print(result)

# print(__file__)
# print(__name__)



