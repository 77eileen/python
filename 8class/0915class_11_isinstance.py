#isinstance(),클래스변수,클래스함수
#상속 :어떤 클래스를 기반으로 그 속성과 기능을 물려받아 새로운 클래스 만드는 것
#isinstance() 함수 :객체가 특정 클래스의 인스턴스(객체)인지 확인하는데 사용
#사용하는 이유
#1. 타입확인 : 함수나 메서드가 특정 클래스의 인스턴스를 기대할 때, 이를 확인
#2. 다형성 : 상속 관계에 있는 클래스들 간에 공통된 인터페이스를 제공할 때, instance 

class Student:
    def study (self):
        return "공부 중입니다."
class Teacher:
    def teach(self):
        return "가르치는 중입니다."
    
# 리스트에 어떤 객체가 있는지 모를 때, 특정 인스턴스만 기대할 수 없다
peoples = [Student(), Teacher(), Student()]
# del peoples[0]
if isinstance(peoples[0], Student):
    print (peoples[0].study())
else:
    print (peoples[0].teach())


#str() 함수


