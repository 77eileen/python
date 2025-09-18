class Student:
    # 클래스 변수 선언
    school_name = "파이썬 고등학교"    # 모든 학생이 공유하는 학교 이름
    total_students = 0                # 전체 학생 수를 세는 변수

    def __init__(self, name, grade):
        # 인스턴스 변수 선언
        self.name = name      # 각 학생의 이름
        self.grade = grade    # 각 학생의 학년
        Student.total_students += 1    # 학생이 생성될 때마다 전체 학생 수 증가

# 학생 인스턴스 생성
student1 = Student("김철수", 1)
student2 = Student("이영희", 2)

# 클래스 변수 출력
print(f"학교 이름: {Student.school_name}")
print(f"전체 학생 수: {Student.total_students}")

# 인스턴스 변수 출력
print(f"\n1번 학생 정보:")
print(f"이름: {student1.name}")
print(f"학년: {student1.grade}")

print(f"\n2번 학생 정보:")
print(f"이름: {student2.name}")
print(f"학년: {student2.grade}")

# 학교 이름 변경 (클래스 변수 수정)
Student.school_name = "파이썬 중학교"
print(f"\n학교 이름 변경 후: {Student.school_name}")
# 모든 학생의 학교 이름이 변경됨
print(f"student1의 학교: {student1.school_name}")
print(f"student2의 학교: {student2.school_name}")