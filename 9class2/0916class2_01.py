# 상속
# 상속은 기존 클래스의 속성, 메서드를 새로운 클래스가 물려받아 재사용하는 것
# 상속을 통해 코드의 재사용성을 높이고, 유지보수를 용이하게 할 수 있음
# 상속받는 클래스: 자식 클래스, 서브 클래스
# 상속해주는 클래스: 부모 클래스, 슈퍼 클래스
# 상속 문법: class 자식클래스(부모클래스):
# 다중 상속: class 자식클래스(부모클래스1, 부모클래스2):

# 부모클래스
class Parents:
    def __init__(self,name):
        self.p_name=name # 변수 생성 자체가 'self'로 자기 객체를 통해 만드는 것이기에, 자동으로 물려받을 수 없음
        print('부모생성자')
    def parents_method(self):
        print('부모 클래스 메소드')

class Child(Parents):
    def __init__(self,name,age): # 생성자 안에서는 부모 생성자 호출 가능
        Parents.__init__(self,name) # 부모 클래스 이름.__init__ 또는 super().__init__(name) 으로 써도됨.
        self.age=age
        print('자식생성자')
    def child_method(self):
        print('자식 클래스 메소드')

# child 클래스의 객체 c
c=Child('홍길동',20)
# print(c.p_name) > 일반 상속에서는 '메소드'만 내려온다
print(c.p_name,c.age)