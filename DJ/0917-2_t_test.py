
파이썬 객관식 시험
eileen.class.it@gmail.com 계정 전환
 
비공개
 
초안 저장됨
1. 다음 중 파이썬에서 리스트를 복사하는 올바른 방법은?
0점
b = a
b = a.copy()
b = a[:]
b = list(a)
2.  다음 코드의 출력 결과는?  

x = [1, 2, 3]
y = x
y.append(4)
print(x)
0점
[1, 2, 3]
[1, 2, 3, 4]
[4]
오류 발생
3.  다음 중 파이썬 딕셔너리(dict)에 대한 설명으로 옳지 않은 것은?  
0점
키는 변경 불가능한 객체여야 한다
값은 어떤 자료형이든 가능하다
딕셔너리는 순서를 보장하지 않는다 (Python 3.7 이상 제외)
dict.keys()로 값에 바로 접근할 수 있다
4.  다음 코드의 출력 결과는?  

def func(x, y=[]):
    y.append(x)
    return y

print(func(1))
print(func(2))
0점
[1] [2]
[1] [1, 2]
[1, 2] [2]
오류 발생
5.  다음 코드의 출력 결과는?  

a = [1, 2, 3, 4]
b = list(map(lambda x: x*2, a))
print(b)
0점
[1, 2, 3, 4]
[2, 4, 6, 8]
[1, 4, 9, 16]
[0, 2, 4, 6]
6.   다음 중 올바른 클래스 상속 예제는?  
0점
class Child(Parent): pass
class Child inherits Parent: pass
class Child < Parent:
class Child: Parent
7.  다음 코드의 출력 결과는?  
a = [1, 2, 3, 4]
print([x**2 for x in a if x%2==0])
0점
[1, 4, 9, 16]
[4, 16]
[1, 9]
[2, 4]
8.  다음 중 파이썬의 데코레이터(decorator)에 대한 설명으로 옳은 것은?  
0점
함수 실행 전에 다른 함수를 추가 기능으로 감싸는 문법
클래스에서만 사용 가능
반드시 반환값이 없어야 한다
변수 이름 변경 기능만 수행한다
9.  다음 코드 실행 결과는?  

def multiply_list(lst, n):
    return [x * n for x in lst]

print(multiply_list([1, 2, 3], 3))
0점
[1, 2, 3]
[3, 6, 9]
[1, 4, 9]
[3, 6, 12]
10.  다음 중 올바르게 함수를 정의하고 호출한 것은?
0점
def add(a, b):\n return a + b\nprint(add(2, 3))
def add(a, b):\n print(a + b)\nadd = add(2, 3)
add(a, b):\n return a + b\nprint(add(2, 3))
def add(a, b)\n return a + b\nprint(add(2, 3))
이 콘텐츠는 Google이 만들거나 승인하지 않았습니다. - 양식 소유자에게 문의 - 서비스 약관 - 개인정보처리방침
양식이 의심스러운가요? 보고서

Google 설문지