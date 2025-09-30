numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for num in numbers:
    if num >= 100:
        print(f'100이상의 수 {num}')

print('='*30)



#중첩for문
for i in range(3):
    for num in range(3):
        print(f'i : {i}   num : {num}')
    print()

print('='*30)



#중첩for문 2
list_1 = [11, 33]
list_2 = [10, 30, 40]
list_2th = [list_1, list_2]
print(f'list_2th 는 {list_2th}')


print('='*30)
for row in list_2th:
    print(row)



print('='*30)
print(f'list_2th[1][1]는 {list_2th[1][1]}')
print('='*30)



for i in range(len(list_2th)):
    for j in range(len(list_2th[i])):            #list 2th의 i 범위에서 j만큼 순환. 그래야지 list_1, list_2 갯수 상관없이 순환.
        print(f'list_2th[{i}][{j}] {list_2th[i][j]}')



