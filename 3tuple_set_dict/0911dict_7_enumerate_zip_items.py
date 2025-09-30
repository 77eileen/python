# enumerate()   zip(),   .items()  .keys()  .values()
# map(), 정렬 --> 람다함수를 적용
# 함수의 parameter - 키워드 parameter, 가변 키워드 parameter

list_a = ['사과', '포도', '딸기']
for i in list_a:
    print(i)

print ("============enumerate()==========================")
list_a = ['사과', '포도', '딸기']
for i in enumerate(list_a):
    print(i)                     #튜플 형태로 나옴

for i in enumerate(list_a):
    print(i[0])

for i in enumerate(list_a):
    print(i[1])

for index, value in enumerate(list_a):
    print(f'{index} : {value}')   #딕셔너리 형태?


print ("============zip()==========================")
# zip()  두 개의 리스트 또는 집합을 각 원소별로 묶어준다
names = ['홍길동', '이순신']
ages = [25, 35]
print ( list(zip (names, ages)))   #리스트 [('홍길동', 25), ('이순신', 35)]
print ( dict(zip (names, ages)))   #딕셔너리 {'홍길동': 25, '이순신': 35}

print ("==========for문 ==zip()==========================")
for name,age in zip(names,ages) :
    print (f'name: {name}, age:{age}')

print ("==========  .items()  .keys()  .values() =========================")
# .items()  .keys()  .values()
dict_1 = {'취미':'수영', '좋아하는 음식':'떡볶이'}
print (f'dict_1 = {dict_1}')
print (f'.keys() = {dict_1.keys()}')            #.keys()  key만 출력
print (f'.values() = {dict_1.values()}')        #.values() value만 출력
print (f'.items() = {dict_1.items()}')         # .items()  key, value 둘다 출력

