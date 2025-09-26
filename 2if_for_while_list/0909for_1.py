#순환문 for
#for i range(100):     ===> i는 변수, 0~99까지 리스트 집합의 인덱스0에 대해 i 대입. 인덱스 1에 대해 i 대입. ~~ 인덱스99까지 i 대입 후 종료

for i in range(3):
    print(f'출력 : {i}')  

print ("="*30)

for i in [10,20,50]:
    print(f'출력 : {i}')  

print ("="*30)

#0~100사이의 중복되지 않은 랜덤한 숫자 10개를 리스트로 저장
import random
numbers = random.sample(range(100),10)
print(f'랜덤한 숫자 10개 : {numbers}')

#짝수만 출력
#numbers 데이터 중에 짝수만 찾아서 새로운 리스트에 저장
#1.리스트를 순환한다
#2.순환하면서 각 데이터가 짝수인지 판단한다
#3.짝수이면 미리 준비한 빈 리스트에 추가한다
#4.모든 순환이 끝나면 (for문 끝나면) 준비한 리스트를 출력한다. len()이용해서 갯수도 확인한다.
new_numbers=[]
for num in numbers:
    if num%2==0:           #2로 나눠서 나머지가 0 : 짝수
        new_numbers.append(num)
print(f'랜덤한 숫자 10개 중 짝수는 {new_numbers}, 갯수는 {len(new_numbers)}')