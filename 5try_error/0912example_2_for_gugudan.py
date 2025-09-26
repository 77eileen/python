# 구구단 for문

# 구구단 2단
for i in range(1,10):
    print (f'2 X {i} = {2*i}')

# 구구단 전체I : 1*1, 1*2, 1*3 .... 으로 순환
for i in range(1,10):
    print (f"======= {i}단 I =======")
    for j in range (1,10):
        print (f'구구단 : {i} X {j} = {i*j}')

# 구구단 전체II : 1*1, 2*1, 3*1 ... 으로 순환
print ("======== 구구단 II ========")
for i in range(1,10):
    for j in range (1,10):
        print (f'{j} X {i} = {i*j}', end='\t')
    print()