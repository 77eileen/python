# 학생클래스 생성
# 인스턴스 변수 : 이름, 국 영 수 
# 인스턴스 메서드 : 총점, 평균, 학점, __str__
class Student:
    def __init__ (self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    def get_sum (self):
        return self.kor + self.eng + self.math
    def get_ave (self):
        return self.get_sum() /3
    def grade (self):
        if self.get_ave() >= 90 :
            return ('학점 A')
        elif self.get_ave() >= 80 :
            return ('학점 B')
        elif self.get_ave() >= 70 :
            return ('학점 C')
        elif self.get_ave() >= 60 :
            return ('학점 D')
        else:
            return ('학점 F')
    def __str__(self):
        return f'이름 : {self.name}, 총점: {self.get_sum()}, 평균 : {self.get_ave()}, 학점 : {self.grade()}'

s1 = Student ('홍길동', 90, 80, 60)
print(s1.get_sum())
print(s1.get_ave())
print(s1.grade())
print(s1)
s2 = Student ('영희', 90, 80, 100)
print(s2)
s3 = Student ('철수', 70, 60, 50)
print(s3)
s4 = Student ('짱구', 100, 90, 80)
print(s4)


