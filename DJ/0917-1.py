

# 4️⃣ 딕셔너리, enumerate, map/zip (15~18)
# Q15. (코딩)
# 다음 딕셔너리에서 최고 득표자 이름만 출력하시오. (동점인 경우 모두 출력)
# votes = {"홍길동":3, "이순신":5, "강감찬":5, "율곡":2}
# # 결과: ['이순신', '강감찬']
votes = {"홍길동":3, "이순신":5, "강감찬":5, "율곡":2}
max_p = max (votes.items(), key=votes.values()))
winner = []
for p in max_p:
    if p != winner:
        winner += p
print(winner)



# Q18. (주관식)
# map과 리스트 컴프리헨션을 비교했을 때 장단점을 설명하시오.
=> 쉽고 간단하게 설명해주고 예시도 보여줘.




# Q20. (코딩)
# 학생(Student) 클래스를 정의하시오.
# 속성: 이름, 점수
# 메서드: 평균 점수 반환 (get_avg())
# 여러 학생을 리스트에 담고, 평균 점수가 80 이상인 학생 이름만 출력하시오.
=======> 학생들의 평균을 구하라는 건줄 알았어. 그건 어떻게 해야해? 
class Student:
    def __init__ (self, name, score):
        self.name = name
        self.score = score
    def get_avg (self):
        print (f'평균 점수는 {sum(self.score) / self.score[]+1})

s_list = [Student('철수', 80), Student('영희',100), Student('영호', 200)]
s_list.get_avg()





# Q21. (주관식)
# isinstance(obj, cls) 와 type(obj) == cls 의 차이를 설명하시오.
# class A: pass
# class B(A): pass
# b = B()
# type(b)==A   # False
# isinstance(b,A)  # True

# ===> 풀이
# type(obj) == cls
# “이 물건이 정확히 이 설계도로 만들어졌나?” 물어보는 것
# ===> 예시:
# class A: pass
# class B(A): pass
# b = B()  # B로 만들어진 물건
# type(b) == A  # ❌ False, b는 정확히 B로 만들어짐
# type(b) == B  # ✅ True
# ===> 즉, 정확히 같은 클래스여야 True
# 3️⃣ isinstance(obj, cls)
# “이 물건이 이 설계도 또는 그 설계도로부터 만들어진 것인가?” 물어보는 것
# 상속도 포함해서 체크 가능
# ==> 예시:
# isinstance(b, B)  # ✅ True, B로 만들었으니까
# isinstance(b, A)  # ✅ True, B는 A에서 상속받았으니까

# 🔑 비유
# A = 자동차 설계도, B = 전기 자동차 설계도(A를 상속)
# b = B() → b는 전기 자동차
# type(b) == A? ❌ → b는 정확히 일반 자동차가 아니라 전기 자동차
# isinstance(b, A)? ✅ → 전기 자동차도 자동차 종류니까 맞음


# Q22. (코딩)
# 추상 클래스 Shape을 만들고, area() 추상 메서드를 정의하시오.
# 이를 상속받아 Circle(반지름), Rectangle(가로, 세로) 클래스를 구현하고, 각 도형의 넓이를 출력하시오.





# Q24. (주관식)
# 메서드 오버라이딩(Overriding)과 오버로딩(Overloading)의 차이를 설명하시오.
# 모르겠어 설명해줘
문제: 오버라이딩 vs 오버로딩

정답 / 설명:

오버라이딩(Overriding): 부모 클래스 메서드를 자식 클래스에서 재정의

오버로딩(Overloading): 같은 이름의 메서드를 매개변수 개수/타입에 따라 다르게 정의 (Python에서는 지원 X, 기본값/가변인자로 구현 가능)
===> 이해가 안가. 중학생 수준으로 쉽게 설명해줘. 비유 적절히 해서. 그리고 예시도 보여줘.

# Q25. (코딩)
# 리스트 컴프리헨션을 이용해 1~50 사이의 정수 중 소수(prime number)만 뽑아내는 코드를 작성하시오.
소수를.. 어떻게 만들어야하는지 모르겠는뎅??
컴프리헨션이 아닌 형태로 풀어서 써주고, 
로직 하나마다 자세히 설명해줘