# 집합을 이루는 요소 : 숫자, 문자, 문자열, list, set, tuple
[1, 1.5, "1212", "2", [1,2,3], (4,8,9), {3,7}]
# dict 키와 값의 쌍으로 구성
# {key:value, key:value}   
# 순서가 없다. (set의 성질 가짐)
#   key
#     : 중복안됨
#     : 변하지 않는 것만 가능 (문자열, 숫자, 튜플 / a=1 과 같은 변수 사용 불가)
#   value
#     : 중복가능
# CRUD 가능 (create, read, update, delete)
# 각 요소에 접근할 때는 key로 접근 (인덱스가 아님)

student = {
    "name" : "홍길동",
    "age" : 20,
    "major" : "컴퓨터"
}

print ("읽기=================")
#읽기
print (f"student[name]={student['name']}")

print ("업데이트=================")
#업데이트 : 기존 key값이 있으면 업데이트되고 key가 없으면 추가.
student["name"] = '이순신'
print(student)

print ("삭제=================")
#삭제
del student['major']
print(student)

print ("추가=================")
#추가 : 기존 key값이 있으면 업데이트되고 key가 없으면 추가.
student['add'] = '서울시 강남구'
print (student)