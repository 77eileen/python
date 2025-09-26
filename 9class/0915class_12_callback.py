# 클래스의 콜백함수
# 객체끼리 비교 (따로 정의하지 않으면, 객체의 주소값을 비교함)
# __eq__   :   ==   같다
# __ne__   :   !=   같지않다
# __gt__   :   >    크다
# __ge__   :   >=   크거나 같다
# __le__   :   <=   작거나 같다
# __lt__   :   <    작다

class Student:
    def __init__ (self, name, score):
        self.name=name
        self.score=score
    def __str__(self):
        return f'이름: {self.name}, 점수:{self.score}'
    def __eq__ (self, other): 
        return self.name == other.name       #eq 정의를 이름이 같은것으로 정의함.

s1=Student('길동', 80)
s2=Student('이순신', 100)
print(s1.__str__())
print(s2.__str__())
print(s1==s2)