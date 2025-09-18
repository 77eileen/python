# 🧩 실습 문제: 재고 관리 시스템 만들기
# 🎯 전체 목표
# 재고 관리 시스템 클래스를 구현하라.
# 🧱 1단계 — 상품 클래스 구현
# 목표: 상품 정보를 관리하는 클래스를 구현하라.
# 설계:
# 속성: name (상품명), price (가격), quantity (수량)
# 메서드: get_info() (상품 정보 출력)

class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def get_info(self):
        return (f'상품명 : {self.name}, 가격 : {self.price}, 수량 : {self.quantity}')
#2단계 : 재고관리 클래스
#Inventory 클래스를 만들어 여러 상품을 관리하도록 합니다.
#필요한 기능
# products 속성 — 상품 리스트를 저장
# add_product(product) — 상품 추가
# remove_product(product_name) — 상품 제거
# get_inventory() — 전체 상품 정보 출력


class Inventory:
    def __init__ (self):
        self.products= []
    def add_product(self,product):
        self.products.append(product)
    def remove_product(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]
    def get_inventory(self):
        for p in self.products:
            print(p.get_info())

# 3단계 — 판매 기능 추가
# 목표
# Inventory 클래스에서 상품을 판매할 수 있는 기능을 추가하는 것
# 요구사항
# 메서드 이름: sell_product(product_name, quantity)
# 동작:
# product_name에 해당하는 상품이 존재하면
# 재고(quantity)가 충분하면 판매하고 재고 차감
# 부족하면 "재고 부족" 메시지 출력
# 상품이 없으면 "상품 없음" 메시지 출력
    def sell_product (self, product_name, quantity):
        for p in self.products:
            if p.name == product_name:
                if p.quantity >= quantity:
                    p.quantity -= quantity
                    print(f"{product_name} {quantity}개 판매 완료")
                    return
                else:
                    print("재고 부족")
                    return
        print("상품 없음")


# 4단계 — 재고 부족 알림 기능
# 목표
# 재고가 0이 된 상품을 확인하고,
# "상품명 재고 없음" 메시지를 출력하는 기능 추가
# 설계 힌트
# 메서드 이름: check_inventory()
# 동작:
# self.products 리스트를 반복
# p.quantity == 0이면 메시지 출력
# 출력 예시: "포도 재고 없음"

    def check_inventory(self):
        for p in self.products:
            print (p.get_info())
            if p.quantity == 0 :
                print(f"{p.name} 재고 없음")

# 각 선택지마다 기존에 구현한 메서드 호출
# 상품 추가 → add_product()
# 상품 제거 → remove_product()
# 상품 판매 → sell_product()
# 재고 확인 → check_inventory()
# 반복 종료: 사용자가 5 선택 또는 "N" 입력 시 종료
# 힌트
# 반복: while True:
# 사용자 입력: input()
# 선택지 분기: if / elif / else
# 상품 입력: 이름, 가격, 수량을 input()으로 받음
# 판매 시 수량 입력: input() 후 int() 변환

    def run(self):
        while True:
            # 나중에 메뉴 코드 넣을 자리
            choice = input("상품추가(1), 상품제거(2), 상품판매(3), 재고확인(4), 종료(5) => 번호 선택: ")
            if choice == "5":  # 종료 번호
                break
            elif choice == "1":
                name = input("상품명: ")
                price = int(input('가격: '))
                quantity = int(input('수량: '))
                self.add_product(Product(name,price, quantity))
            elif choice == "2":
                name = input('제거할 상품명: ')
                self.remove_product(name)
            elif choice == "3":
                name = input('판매할 상품명: ')
                quantity = int(input("수량: "))
                self.sell_product(name, quantity)
            elif choice == "4":
                self.check_inventory()
            else:
                print('잘못된 입력입니다.')

# 3️⃣ 객체 생성 + 초기 상품 추가
store = Inventory()
store.add_product(Product("포도", 15000, 10))
store.add_product(Product("사과", 20000, 5))
store.add_product(Product("수박", 30000, 8))

# 4️⃣ 프로그램 실행
store.run()