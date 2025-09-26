#랜덤 라이브러리 가져오기 (import라는 공구상자에서 random도구를 빼내옴.)
import random

#랜덤 라이브러리중에서 sample 함수 호출 
random_numbers=random.sample(range(100),5)  #0~99 범위에서 중복되지 않은 랜덤한 5개 추출

#랜덤 라이브러리중에서 randint 함수 호출 
random_int= random.randint(0,10) #0~10 사이 중에서 랜덤하게 정수형 1개 추출

#append 추가
random_numbers.append(random_int)

#50이 list에 포함되어 있는지 확인하는 방법
print(f'50 포함여부: {50 in random_numbers}')
print(random_numbers)

print('=='*30)

#삭제
#인덱스로 제거하기 : del 키워드, pop()함수
#1. del 리스트명[인덱스] : 메모리에서도 없어짐.
del random_numbers[0]
#del_removed_number = del random_numbers[0]  #메모리에서 사라지므로 확인 불가
#print(del_removed_number)                   #메모리에서 사라지므로 확인 불가
print(f'del이용 [0]삭제 : {random_numbers}')

#리스트명.pop(인덱스) : 삭제하더라도 메모리에 저장되서 다시 캐내올 수 있음.
pop_removed_number=random_numbers.pop(3)
print(pop_removed_number)                    #삭제해도 메모리에 저장되므로 확인 가능
print(f'pop이용 [3]삭제 : {random_numbers}')


