#C.R.U.D : Create, Read, Update, Delete
#리스트
age=20
array = [273, 32, 103, '문자열', True, False, age]   #age 변수
print(array)   #age 변수값이 출력됨
print(array[3][2]) #'문자열'에서 '열'만 출력가능

print('===============')

array_2=[100,array]
print(array_2)

print('===============')

print(array_2[1][3])  #[100, [273, 32, 103, '문자열', True, False, 20]] 여기서 문자열 불러오는 인덱싱.

print('===============')

temp = [
    [1,2],      #temp[0]
    [10,20],    #temp[1][1] 하면 값20 / temp[1,1] 안됨
    [30,40]     #temp[2]
    ]
print(temp[1][1])
# print(temp[1,1])  #안됨. nonpi? 에서는 가능 (nonpi? pandas? : 데이터분석할때 사용)

print('===============')

list_a=[273, 32, 103, '안녕', True, False]
print(list_a[1:4])
print(list_a[3][0])

