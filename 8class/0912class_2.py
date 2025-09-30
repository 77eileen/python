#클래스 내에서 인스턴스 변수 만들기
class People():
    def make_instance(self):    #self가 하기에서 h1임. self 필수.
        self.name = None
        self.age = None
        self.addr = None

h1 = People()
h1.make_instance()   #==>오류x : h1.make_instance() 인스턴스를 실행하고 나서 거기에 있는 메서드를 사용해서 print출력
print(h1.addr)

h2 = People()
print(h2.addr)    #==>오류: h2.make_instance() 인스턴스를 실행시키지 않았으니까. 

