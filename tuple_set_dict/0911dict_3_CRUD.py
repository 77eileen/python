# 딕셔너리 생성
# 딕셔너리에서 값을 출력
# 딕셔너리에서 값을 추가
# 딕셔너리 삭제
# 딕녀너리 특정 키의 데이터를 수정

print ("dict 생성=================")
name = ['철수', '영희', '순희']
role = ['부반장', '반장', '미화반장']
students_info ={}
for i in range(len(name)):
    students_info[name[i]] = role[i]
print(students_info)

print ("dict 값 출력 =================")
print(students_info['영희'])

print ("dict 값 업데이트 및 추가 =================")
students_info['철수'] = '체육부장'
students_info['영수'] = '부반장'
students_info['광수'] = '오락부장'
print(students_info)

print ("dict 삭제 =================")
del students_info['철수']
print(students_info)




print ("=========================================================================")
# 딕셔너리 생성
# 딕셔너리에서 값을 출력
# 딕셔너리에서 값을 추가
# 딕셔너리 삭제
# 딕녀너리 특정 키의 데이터를 수정
my_bag={"필통":"파란색", "공책":"수학공책", "지갑":"분홍색"}
# 출력 
print(my_bag)
# 가방에서 필통을 꺼내서 출력
print (f"필통 : {my_bag['필통']}")
# 가방에서 공책을 꺼내서 출력
print (f'공책 : {my_bag["공책"]}')
# 지갑이 오래되서 "가죽지갑"으로 변경
my_bag['지갑'] = '가죽지갑'
print (f'지갑변경 : {my_bag}')
# 물통은 추가 하얀색
my_bag['물통'] = '하얀색'
print (f'물통 추가 : {my_bag}')
# 공책을 다써써 버리기
del my_bag['공책']
print (f'공책 버리기 : {my_bag}')


print ("=========================================================================")
# 순환문과 연결
for i in my_bag:
    print(f'my_bag의 순환문 결과 : {i}')         #key 값만 출력됨
    print(f'key={i} value={my_bag[i]}')

# 순환문과 연결, value 출력
for i in my_bag.values():
    print(f'my_bag.values()의 순환문 결과 : {i}')         #value 값만 출력됨

# 순환문과 연결, key 출력
for i in my_bag.keys():
    print(f'my_bag.keys()의 순환문 결과 : {i}')         #key 값만 출력됨


# 순환문과 연결, key 출력
for i in my_bag.items():
    print(f'my_bag.items()의 순환문 결과 : {i}')         #key 값만 출력됨





