# # # 리스트 컴프리핸션
# # total = []
# # for i in range(1,11):
# #     total.append(i)
# # print(total)

# print([i for i in range(1,11)]) # 이것이 리스트 컴프리핸션
# # 컴프리핸션이란 '한 줄'로 표현하는 방법임

import random

total=[]
for i in range(5):
    total.append(random.randint(1,10))

print([ random.randint(1,10) for i in range(5)])