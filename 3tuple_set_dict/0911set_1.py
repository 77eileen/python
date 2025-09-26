# set
# 저금통
list_a = [100, 500, 10, 500, 100, 50, 500, 10]
# 저금통에 있는 동전의 종류 10,50,100,500원

print ("1=================")
# ref. set을 안쓰는 경우.
list_coin = []
for i in list_a:
    if i in list_a and not i in list_coin:
        list_coin.append(i)
print(f'set을 사용하지 않고 종류 확인결과 {list_coin}')

print ("2=================")
#set : 중복을 제거함. (중복을 허용하지 않음)
set_a={1,2,3,1,2,3,1}
print(f'set_a = {set_a}')

print ("3=================")
print (set(list_a))


print ("4=================")
# set_a[0] : set은 순서를 보장하지 않기 때문에 인덱싱 불가. add, append, insert 불가. 
# print(set_a[0])  ==> TypeError: 'set' object is not subscriptable
# add : 추가, update : 값을 변경
set_2 = {1,2,4,5,6}
set_2.add(3)   #순서 보장없이 add 됨. append처럼 마지막에 붙지않음. 어디들어갈지 모름.
print(set_2)   
set_2.remove(2)
print(set_2)
print ("5=================")
print(set_2.pop())  
# 리스트에서 팝 인덱스를 넣어서 실행가능했으나, set에서는 인덱스 지정없이.
# set.pop() 은 집합에서 임의의 원소 하나만 꺼내고 제거하는 메서드입니다.
# 즉, pop()은 한 번 호출할 때 하나만 반환합니다. (리스트의 pop()처럼)
# 지금 상황에서는 {1, 3, 4} 중에서 1이 가장 먼저 저장된 버킷에 있었기 때문에 1이 나온 겁니다.
# 즉, pop()의 결과는 예측 불가능하다고 생각해야 합니다.
set_2.pop()
print(set_2)