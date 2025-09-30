# #remove : 리스트.remove(값) 값을 제거.
list_1=[10, 20, 30, 40]
list_1.remove(20)
print(list_1)

print("="*30)
for i in range (5, -1, -1):  #5에서부터 역순으로 for문 순환
    print(i)

print("="*30)

#리스트에서 1을 삭제하는 방법.
list_a =[1,1,1,2]
for i in range(len(list_a)-1,-1,-1) :   #역순으로 하지 않고 순차적으로 하게되면 인덱스0,1,2 의 값이 계속 바뀌기 때문에, 뒤에서 역순으로 순환하면 앞에 인덱스의 값이 변하지 않음
    if list_a[i] == 1:
        del list_a[i]
print(list_a)

print("="*30)

#remove
list_b=[1,1,1,2]
for i in range(len(list_b)):
   print(list_b)
   if 1 in list_b:
      list_b.remove(1)
print(list_b)

#remove #순환구조가 깨질것 같은 로직에서 정방향 순환은 무조건 len으로! 
#for문안에서는 순환구조가 깨지지 않도록 로직을 짜야함. 
list_c=[1,1,1,2]
for i in list_c:          #len을 안하게 되면 list_c에서 i돌면서 첫번째1 를 삭제하고 나면 [1,1,2]가 남는데, 여기서 첫번째1은 인덱스0에 대한 값이므로 두번째 순환때는 인덱스1번째 1이 삭제되므로 두번째 1이 계속 남게됨. 
   print(list_c)
   if 1 in list_c:
      list_c.remove(1)
print(list_c)

#remove - break
list_d=[1,1,1,1,2,2,2,2,2,2,2,2,2,2,2]
for i in range(len(list_d)):
    print("*")
    if 1 in list_d:
       list_d.remove(1)
    else:
        break              #break를 안해주면 list_d에 값이 있는만큼 계속 순환하게 됨. 1이 없을 때는 break 되도록 해놓으면 list_d만큼 순환하지않음.
print(list_d)

