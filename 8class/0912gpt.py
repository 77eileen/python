# 클래스 실습 문제
# 1. 자동차 클래스 만들기
class Car():
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def info(self):
        print (f'자동차 정보: {self.brand}, {self.model}, {self.year}')

car_1 = Car('현대', '아반떼', '2025년형')
car_1.info()


# 2. 은행 계좌 클래스 만들기
# 속성: owner, balance
# 메서드: deposit(amount), withdraw(amount)
# 조건: 출금 시 잔액 부족하면 "잔액 부족" 메시지 출력
class Bankacount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit (self, amount):
        self.balance += amount
        print(f'{amount}원이 입금되었습니다. 잔액: {self.balance}')
    def withdraw (self, amount):
        if amount > self.balance:
            print ('잔액 부족')
        else:
            self.balance -= amount
            print(f'{amount}원이 출금되었습니다. 잔액: {self.balance}')
    def info(self):
        print(f"계좌주 : {self.owner}, 잔액: {self.balance}")
p1 = Bankacount('홍길동', 30000)
p1.info()
p1.deposit(20000)
p1.withdraw(10000)

# 3. 직원(Employee) 클래스 만들기
# 클래스 변수: employee_count (직원 수 카운트)
# 인스턴스 변수: name, salary
# 메서드: info() → 직원 이름과 연봉 출력
# 직원이 새로 생성될 때마다 employee_count 증가
class Employee():
    employee_count = 0
    def __init__(self, name, salary):
        Employee.employee_count +=1
        self.name = name
        self.salary = salary
    def info (self):
        print(f'총 직원수 : {self.employee_count}, 직원이름 : {self.name}, 직원연봉 : {self.salary}')

p1 = Employee('지은탁', '6000만원')
p1.info()


# 4.도서(Book) 클래스 만들기
# 속성: title, author, price
# 메서드: discount(rate) → 주어진 할인율(rate, %)만큼 가격을 깎아 반환
class Book():
    def __init__ (self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.rate = 0
    def discount (self, rate):
        self.rate = rate
        self.price = self.price*(1-self.rate)
        return self.price
    def info (self):
        print (f'{self.title}/{self.author} 작가님의 책 가격은 {int(self.rate*100)}% 할인된 {self.price}원 입니다.')

b1 = Book('나의 장래희망은 귀여운 할머니', '하정', 18000)
b1.discount(0.1)
b1.info()
