# 클래스
# 클래스 변수, 인스턴스 변수
# 생성자 __init__
# 메소드  __str__   / __eq__ / __ne__ / __lt__ / __gt__ / __le__ / __ge__
# property :  getter, setter, deleter, private --> 함수를 변수처럼 사용
# 객체생성

# 상품관리 클래스명 Product
# 상품명 product_name, 가격 product_price, 재고 product_stock
class Product():
    def __init__ (self, product_name, product_price, product_stock):
        self.product_name = product_name
        self._product_price = product_price
        self.product_stock = product_stock

    @property
    def product_price(self):
        return self._product_price
    @product_price.setter
    def product_price(self, value):
        if value < 0:
            print("가격은 0보다 작을 수 없습니다.")
        else:
            self._product_price = value


    def check_product_stock (self):
        if self.product_stock <= 0 :
            return '재고가 없습니다.'
        elif self.product_stock == 1:
            return '마지막 하나 남아있습니다.'
        else:
            return '2개 이상 남아있습니다.'
        
    def __str__ (self):
        return f'상품명 : {self.product_name}, 가격 : {self._product_price}, 재고 : {self.product_stock}, 알람:{self.check_product_stock()}'
   
    def __repr__(self):
        return self.__str__()
    
    def __eq__ (self, other):
        return self.product_price == other.product_price
        
products =[
    Product('공책', 2000, 1),
    Product('연필', 2000, 3),
    Product('지우개', 500, 10)
    ]

print(products.__str__())
print(products)

# p1 = Product('공책', 2000, 1)
# p2 = Product('연필', 2000, 3)
# print(p1.__str__())
# print(p2.__str__())
# print(p1 == p2)


print('===공책 가격을 20% 인하===')
products[0].product_price = products[0].product_price*0.8
print(products[0])

print('===지우개 재고를 100 추가===')
products[2].product_stock += 100
print(products[2])

print('===전체 제품 출력===')
for i in products:
    print (i.__str__())


print('===제품 추가===')
products.append (Product('일기장', 2000, 20))
products.extend ([Product('삼색볼펜', 5000, 100), Product('샤프', 3000, 1)])
print(products)

print('===제품 삭제===')
del products[-1]
print(products)

print('===모든 제품의 제품 수량===')
product_count=0
for i in products:
    product_count += i.product_stock
print(product_count)


#가격X 수량을 기준으로 같다 크다 크거나같다 작다 작거나같다