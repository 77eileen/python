print ("1=================")
# list, set, tuple, dict
result = dict([['name', '홍길동'], ['age', 20]])
print(type(result))
print(result) 


print ("2=================")
# 두개의 리스트는 한개는 키에 해당하는 값들의 집합
# 다른 하나는 값에 해당하는 집합
# 이걸 dict 구조로 만들려면 
names=['유관순', '이순신', '강감찬']
scores = [100, 99, 98]

# 비어있는 dict 변수를 생성
# 변수 ['key'] = 값 형태로 생성 - 순환문을 통해서

# 방법1
students={}
count = 0
for name in names:
   students [name] = scores [count]
   count += 1
print(f'count 사용 결과 : {students}')

# 방법2
students={}
for i in range(len(names)):
    students[names[i]] = scores[i]
print(f'range len 사용 결과 : {students}')