# 튜플 (고정된 값, 읽기전용)
tuple_1 = (1,2,3,4,1,3,2,1,4)
print(tuple_1[0])
#tuple_1[0]=100   #TypeError: 'tuple' object does not support item assignment => append , insert 함수 불가능
print(tuple_1.count(1))   #튜플 값 중에서 1이 몇 개인지 확인.
print(tuple_1.index(4))   #튜플 값 중에서 가장 처음 나오는 4의 자리가 몇번째 인덱스에 있는지 확인

print ('1================================')

# 튜플과 리스트는 서로 변경이 가능하다.
# 튜플 -> 리스트 O / 리스트 -> 튜플 O

print (type(tuple_1))
print (list(tuple_1))
print (type(list(tuple_1)))

print ('2================================')

list_a = [1,2,3]
tuple_a = (10,20,30)
print(f'type(list_a) = {type(list_a)}')
print(f'type(tuple_a) = {type(tuple_a)}')

print(type(tuple (list_a)))  #list_a 자체가 튜플로 바뀌는게 아니라, 값이 tuple데이터 형태로 반환. 원본의 성질이 바뀌지는 않는다.
list_a = tuple(list_a)  #이렇게하면 list_a 자체가 튜플로 변경됨. 
print(type(list_a)) 




    