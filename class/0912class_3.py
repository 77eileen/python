print ("=======================================================")
#클래스 내에서 인스턴스 변수 만들기
class People():
    def __init__(self):    #self가 하기에서 h1임. self 필수.
        self.name = None
        self.age = None
        self.addr = None
        print('생성자 호출')

print('h1 객체 생성 전')
h1 = People()
print('h1 객체 생성 후')  # ==> 객체가 생성되어서 터미널에 생성자 호출이 실행됨.
print(h1.addr)

#앞선 파일에서는 (class_2) h1.make_instance() 인스턴스를 실행시키지 않아서 오류가 생겼으나,
#def __init__ 으로 만들어줬기 때문에 h1.addr 로도 생성자가 호출이 됨. 

print ("=======================================================")
class Product():
    serial_num = 0           #클래스 변수  
    def __init__(self):        #__init__ 생성자 : 객체 생성할 때 인스턴스 변수를 지정하기 위해 생성자를 만듬. 
        Product.serial_num += 1
        self.serial_num = Product.serial_num    #self.serial_num  인스턴스 변수
        self.name = None

tv1 = Product()
tv2 = Product()
tv3 = Product()
print (tv1.serial_num, tv2.serial_num, tv3.serial_num)


# # ### ✅ 객체(object)
# 프로그래밍 세계에서 “무언가를 표현하는 단위”.
# 속성(변수)과 동작(메서드)을 가질 수 있음.
# 예: s1 = StudentMng() → s1은 객체.
# ---\


# # ### ✅ 인스턴스(instance)
# “객체”라는 큰 개념 안에서, 특정 클래스 설계도로 찍혀 나온 객체를 가리킬 때 쓰는 말.
# 즉, 모든 인스턴스는 객체이지만, 모든 객체가 인스턴스인 건 아님.
# 파이썬 기본 자료형(예: 정수 10)도 객체이긴 하지만, 우리가 정의한 클래스의 인스턴스는 아님.
# ---
# 

# # # ### ✅ 인스턴스 변수(instance variable)
# 객체(인스턴스) 각각이 독립적으로 갖는 변수.
# self를 통해 정의되고, s1.name, s2.name처럼 인스턴스마다 다를 수 있음.
# ---
# # ### 🔎 비유
# 클래스 = 붕어빵 틀
# 인스턴스 = 틀로 찍어낸 붕어빵 (객체)
# 클래스 변수 = 틀 자체에 새겨진 무늬 → 찍히는 모든 붕어빵이 공유
# 인스턴스 변수 = 붕어빵 속에 넣은 앙금 → 붕어빵마다 다를 수 있음
# ---


# 👉 그래서 정리하면:
# 객체 = 넓은 말, “속성과 메서드를 가진 모든 것”
# 인스턴스 = 특정 클래스에서 생성된 객체
# 인스턴스 변수 = 그 인스턴스만 독립적으로 가지는 속성