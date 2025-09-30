list_a=[1,2,"문자열",True,False]
print(list_a[2][2]) #'문자열'에서 '열'출력
print(list_a[:]) #start_index : end_index-1 #원본을 복사
print('==========')
print(list_a[:3])
print(list_a[3:])
print('==========')
print(list_a[-2])
print(list_a[-2:])
#star index : end index-1 : step 1 (상기에는 step1이 생략)
print('==========')
print(list_a[::2])
print(list_a[::-1]) #뒤에서부터 거꾸로 출력


print('==========')

list_b=[1,2,3]
list_c=[4,8,3]
last_name = '홍'
first_name = '길동' 
#리스트연산 : int ==> 변경 가능한 객체
print(f'list_b + list_c = {list_b+list_c}')  #nonpi? 에서는 결과가 5, 10, 6 으로 나옴
print(f'list_b*3 = {list_b*3}')          #nonpi? 에서는 결과가 3, 6, 9로 나옴
#리스트연산 : 문자열 ==> 변경 불가능한 객체
print(f'last_name + first_name = {last_name + first_name}')
print(f'last_name*3 = {last_name*3}')

print('==========')

#실제 사칙연산으로 결과가 나오게 하려면....
list_d = [
    list_b[0]+list_c[0],
    list_b[1]+list_c[1],
    list_b[2]+list_c[2]]
print(list_d)

#append() 함수 : 리스트 뒤에 요소를 추가
#리스트명.append(요소)
#insert() 함수 : 리스트 중간에 요소를 추가 / 잘 사용하지 않음.
#리스트명.insert(위치, 요소)
#변수.뒤에 오는것을 멤버 연산자

print('='*20)

list_e = [1,2,3]
#리스트 뒤에 요소 추가하기
print('# 리스트 "뒤에" 요소 추가하기')
list_e.append(4)
list_e.append(5)
print(list_e)

print('='*20)

#리스트 중간에 요소 추가하기
print('# 리스트 "중간에" 요소 추가하기')
list_e.insert(0,10)
print(list_e)

print('='*20)

list_f = [1,2,3]
list_f.append([4,5,6])
print(f'append로 했을 경우, 리스트 형태로 추가됨. {list_f}') 

list_f.extend([4,5,6])
print(f'extend로 했을 경우, 리스트 형태가 아닌 리스트안의 값이 추가됨. {list_f}')
# 하기와 같이 작성해도 상기 extend 와 동일한 형태로 값만 추가 가능.
list_f += [4,5,6]
print(list_f)



