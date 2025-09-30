# 직원 Employee - ID, 이름, 기본급
class Employee:
    def __init__(self,id,name,base_salary):
        self.id=id
        self.name=name
        self._base_salary = base_salary # private의 의미로 사용
    
    @property
    def base_salary(self):
        return self._base_salary
    @base_salary.setter
    def base_salary(self,money):
        if money > 0:
            self._base_salary=money
        else:
            raise ValueError('금액은 양수입니다')

    def emp(self):
        print('직원클래스')

    def __str__(self):
        return f'{self.name}:{self.id},{self.base_salary}'

# 정규직 FullTimeEmployee - 보너스
class FullTimeEmployee(Employee):
    def __init__(self,id,name,base_salary,bonus):
        super().__init__(id,name,base_salary)
        self._bonus = bonus
    # 보너스도 마이너스 입력 불가
    @property
    def bonus(self):
        return self._bonus
    @bonus.setter
    def bonus(self,valuse):
        if valuse>0:
            self._bonus=valuse
        else:
            raise ValueError('양수만 가능합니다')
    def __str__(self):
        return super().__str__()+f',{self.bonus}'
    def show_class(self):
        print('정규직클래스')

# 계약직 PartTimeEmployee- 시간당 급여
class PartTimeEmployee(Employee):
    def __init__(self, id, name, hourly_rate, hours):
        base_salary = hourly_rate * hours
        super().__init__(id, name, base_salary)
        self._hourly_rate = hourly_rate
        self._hours = hours
    # 시간당 급여 쪽도 getter setter
    @property
    def hourly_rate(self):
        return self._hourly_rate
    @hourly_rate.setter
    def hourly_rate(self,money):
        if money > 0:
            self._hourly_rate=money
        else:
            raise ValueError('양수만 가능합니다')

    @property
    def hours(self):
        return self._hours
    @hours.setter
    def hours(self,money):
        if money > 0 :
            self._hours=money
        else:
            raise ValueError('양수만 가능합니다')
        
    def __str__(self):
        return f'{self.name}{self.id}{self.hourly_rate}{self.hours}'
    def show_class(self):
        print('계약직클래스')

# 인턴 Intern - 고정 수당
class Intern(Employee):
    def __init__(self, id, name, fix_salary):
        super().__init__(id, name, 0)
        self.fix_salary=fix_salary
    def __str__(self):
        return f'{self.name}{self.id}{self.fix_salary}'
    def show_class(self):
        print('인턴클래스')

# 정규직 직원, 계약직, 인턴을 모두 리스트에 섞어서 객체를 저장
# emp = [
#     FullTimeEmployee(),PartTimeEmployee(),Intern()...
# ]
# emp에 들어있는 직원이 각각 어떤 클래스인지, 순환문을 이용하여 각 클래스의 int나 pte와 같은 메소드를 출력할 것.

emp=[FullTimeEmployee(4527,'김철수',4500000,200000),
     Intern(184,'정기소',1520000),
     PartTimeEmployee(1852,'이가영',1548651,8),
     Intern(885,'이수영',1538000),
     FullTimeEmployee(1248,'소각장',4200000,150000)]

# for i in emp:
#     if isinstance(i,FullTimeEmployee):
#         i.fte()
#     elif isinstance(i,Intern):
#         i.int()
#     elif isinstance(i,PartTimeEmployee):
#         i.pte()
#     else:
#         print('회사 직원이 아닙니다.')

for e in emp:
    e.show_class() # emp 리스트의 각각의 객체에 해당하는 메소드를 호출 (다형성)
