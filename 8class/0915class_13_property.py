# 프라이빗 변수와 게터/세터
# 파이썬 클래스에서 getter setter 사용법
import random
class Person:
    def __init__ (self, name, age):
        self.name = name
        self._age = age              #self._age 프라이빗 변수로 만듬. (외부에서 접근 못하게 숨겨둔 변수)

    # def set_age (self, age):
    #     if age < 0:
    #         print ('나이는 음수가 될 수 없습니다.')
    #     else: 
    #         self.age = age     #========>  변수에 값을 썼는데 (ex. p.age = 30 등), 함수가 호출되도록 해보자! ==> 데코레이션(?)이라함.

    @property   #이건 propery 속성이 getter 속성임.
    def age(self):
        return self._age
    
    @age.setter      #setter를 지정해줘야지 p1.age = 30 값을 받을 수 있음.
    def age(self, value):
        self._age = value
    
p1= Person("홍길동", 25)
# print(p1.age())    # ==> 상기 __init__ 에 있는 age 함수 (인스턴스 변수로)가 호출되서 오류남. => self.age=age 를 self._age로 변경 => 25출력
print(p1.age)  # ==> 함수 이름이 출력됨 <bound method Person.age of <__main__.Person object at 0x000001D7FDE76A50>>
               # ==> 함수 이름만 써도 함수를 호출하기 위해 ==> @property 와 _age로 작성 ==> 함수가 호출되면서 25출력 
#property : 메서드를 메서드로 쓰는게 아니라, 호출방법을 함수 이름만 가지고 호출하기위해..!
p1.age = 30 #property 'age' of 'Person' object has no setter : Person 객체의 age 프러퍼티는 세터를 가지고 있지 않다.
print(p1.age) #==> setter 작성 후 상기 p1.age=30 이 적용되어서 출력됨.
#게터, 세터 : 함수를 변수처럼 사용! 사용자는 변수처럼 작성하는데, 실제로는 함수로 작동하기 위해서 이 기능을 씀. 
#@property, @setter는 쌍으로 사용함.

# del p1.age  #오류 property 'age' of 'Person' object has no deleter
print(p1.name)
del p1.name   #propery 속성이 아니므로 삭제가능함.
print(p1.name) #삭제되어서 오류발생됨. 'Person' object has no attribute 'name'





    #     self._name = name   #private 변수로 설정
    #     self._age = age     #private 변수로 설정

    # #데코레이터를 이용한 setter
    # @property
    # def name (self):
    #     return                
    # @name.setter
    # def name(self,name):    #사용자는 (밖에서는) .name 변수를 입력하면 이 함수를 발동시켜서 결과를 출력함.



# a= Person("홍길동", 25)
# print(a.__name)    #직접 접근 (권장되지 않음)

# getter 메서드
# def get_name (self):
#     return self._name

# def get_age (self):
#     return self.age

# def set_name (self, name):



#============ 챗 지피티 ==========================
# 1. "속성" = 사람의 정보
# 예를 들어 사람이라는 객체를 생각해보세요.
# 이름
# 나이
# 키
# 이런 게 다 **속성(특징, 정보)**이에요.
# 👉 즉, "속성 접근" = "사람의 정보를 꺼내거나 바꾸는 것".
# 예:
# p.name → "그 사람 이름 알려줘"
# p.age → "그 사람 나이 알려줘"

# 2. 그냥 변수로 두면 문제 생김
# 예를 들어, 누가 실수로 나이를 음수(-5살)로 바꾸면 어떡하죠? 🤔
# p.age = -5   # 이상하죠?
# 이건 그냥 문이 열려 있어서 아무거나 막 집어넣을 수 있는 상태랑 같아요.
# 안전하지 않아요.

# 3. @property와 @setter = 문지기
# 그래서 집 앞에 문지기를 둡니다.
# 집(객체) 안에는 진짜 값(_age)이 있고
# 문지기(@property, @setter)가 그 값을 주거나 바꿔줘요.
# class Person:
#     def __init__(self, age):
#         self._age = age

#     @property
#     def age(self):  # getter
#         return self._age   # "안에 있는 나이를 보여줌"

#     @age.setter
#     def age(self, value):  # setter
#         if value < 0:
#             raise ValueError("나이는 음수가 될 수 없습니다!")  # 문지기가 막음
#         self._age = value   # 통과되면 나이 저장

# 4. 이렇게 쓰면
# p = Person(20)
# print(p.age)   # 👉 그냥 p.age 라고 쓰면, 사실은 문지기가 값을 건네줌
# p.age = 25     # 👉 그냥 값 바꾸는 것처럼 보이지만, 문지기가 검사하고 넣어줌
# p.age = -5     # 👉 문지기가 "안 돼!" 하고 막아줌

# 5. 비유 요약
# 속성 = 사람의 정보 (이름, 나이, 키 같은 것)
# 속성 접근 = 그 정보를 읽거나 바꾸는 행동
# @property, @setter = 문지기 (그냥 막 접근하지 못하고, 검사를 거치게 만듦)