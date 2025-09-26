# 기본 클래스 생성
class Review:
    # 클래스변수 생성 : 모든 객체들이 공유하는 변수
    count = 0
    # 생성자 메서드 : 객체가 생성될 때 자동으로 호출되는 메서드
    def __init__ (self,name=""):
        self.name = name

#실행가능한 상태를 인스턴스라고 많이 부름. (현업에서)
#객체 생성 = 인스턴스 생성 같은말
#인스턴스 생성
r1 = Review(100)   #상기 __init__ (self)만 기재된 경우. Review.__init__() takes 1 positional argument but 2 were given
r2 = Review("홍길동")
r3 = Review()
#인스턴스 변수 변경
r1.name = "첫번째 리뷰"
print(f'r1 인스턴스 변수 : {r1.name} / r2 인스턴스 변수 : {r2.name} / r3 인스턴스 변수 : {r3.name}')
print(f'현재 클래스 변수 : {Review.count} / r1 클래스 변수 : {r1.count} / r2 클래스 변수 : {r2.count}')   #\ 줄바꿈에 사용. 한줄로 이어지는 효과
#클래스 변수에 접근할 때는 r1. 보다는 Review. 로 접근하는게 좋음.

class Student : 
    pass
    # def __init__ (self):   #pass 인 경우 생략 가능함.
    #     pass
student = Student()

#메소드 : 클래스가 가지고 있는 함수
#class 클래스 이름:
    #def 메소드 이름 (self, 추가적인 매개변수):
        #pass
