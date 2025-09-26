# 학생
# 이름, 학생정보 출력
# 변수 : 이름, 나이
# 함수 : 학생정보 출력

students = []     #학생들 
class StudentMng():
    def __init__(self):       #생성자 매서드
        self.name = ''
        self.age = 0

    def info_student (self):   #인스턴스 매서드
        print (f'이름 : {self.name} / 나이: {self.age}')

s1 = StudentMng()
s1.name = '홍길동'
s1.age = 25
students.append(s1)

s2 = StudentMng()
s2.name = '이순신'
s2.age = 29
students.append(s2)

students[0].info_student()

