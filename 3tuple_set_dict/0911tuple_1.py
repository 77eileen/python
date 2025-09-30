# 얕은 복사 vs. 깊은 복사
def change(obj):
    obj[0] = 100

data = [1,2,3]
change(data)
print (data)
print("================")

a=10
b=a
b=1000
print(f'a={a} b={b}')         #b값을 변화시켜도 a값은 변화되지 않음
print("================")

list_a= [1,2,3]
list_b = list_a       #얕은복사 : list_a 값을 전체 복사하는게 아니라, 값을 가진 링크? 만 복사됨
list_b[0] = 100       #(동기화 복사. list_a 와 동기화 되어서 list_b를 변화시키면 list_a도 바뀜)
print (f'list_a = {list_a} list_b={list_b}')  
print("================")

list_c= [1,2,3]
list_d = list_c.copy()       #깊은 복사 : 값 전체가 복사되어서 동기화 되지 않고, 별도 복사본 파일이 만들어짐.
list_d[0] = 100       
print (f'list_c = {list_c} list_b={list_d}')  