# 집합연산이 가능

print ("1=================")

import random
list_a = random.sample(range(10), 7)
list_b = random.sample(range(10), 7)


find_list =[]
for a in list_a : 
    for b in list_b:
        if a==b:
            find_list.append(a)
print(f'list_a={list_a} / list_b={list_b}')
print(f'find_list = {find_list}')


print ("2=================")

import random
list_c = random.sample(range(10), 7)
list_d = [1,1,1,4,5,6,6,4]


find_list_2 =[]
for c in list_c : 
    for d in list_d:
        if c==d:
            find_list_2.append(c)
print(f'list_c={list_c} / list_d={list_d}')
print(f'find_list_2 = {find_list_2}')


print ("3=================")

find_list_2 =[]
for c in list_c : 
    for d in list_d:
        if c==d:
            find_list_2.append(c)
print(f'list_c={list_c} / list_d={list_d}')
print(f'find_list_2 = {find_list_2}')
print(f'set(find_list_2) = {set(find_list_2)}')

print ("4=================")
# 중복을 허용하면서 0~10 임의의 7개 추출
# random.randint (0,10)  --> 임의의 한개가 추출됨.
list_z = []
for _ in range(7): #여기서는 i역할이 없음. 현업에서는 i를 _ 이렇게 under bar 로 표기함
    list_z.append(random.randint(0,10))
print(list_z)


print ("5=================")
#set을 이용하지 않고, 로직을 개선해서 find_list에서 중복값이 저장되지 않도록 코딩
list_e = random.sample(range(10), 7)  #0~9데이터 중에서 중복되지 않음 임의의 7개
list_f = random.sample(range(10), 7)
find_list_3 =[]
for e in list_e : 
    for f in list_f:
        if e==f and not e in find_list_3 and not f in find_list_3:
            find_list_3.append(e)
print(f'list_e={list_e} / list_f={list_f}')
print(f'set을 사용하지 않고 중복값 찾기 : find_list_3 = {find_list_3}')


print ("6=================")
#합집합
    # 연산자 | (파이프 연산자)  ==> or
set_a = {1,2,3}
set_b = {3,4,5}
union_set = set_a | set_b
print (union_set)
    # 메서드  .union()   (.으로 나오는것도 함수이지만, 독립적으로 사용되지 않은 .append 등을 메서드라 함 / print() 같은건 함수.)
union_set = set_a.union(set_b)
print(union_set)

print ("7=================")
#교집합
set_c, set_d = {1,2,3,4}, {2,3,5}
    # 연산자 &  --> and와 유사한 개념
print(set_c&set_d)
    # 메서드  .intersection()
print(set_c.intersection(set_d))

print ("8=================")
#차집합
    # 연산자 - 
print(set_c - set_d)
    # 메서드  .difference()
print(set_c.difference(set_d))