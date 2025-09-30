print ("=======정렬==============")
# 정렬
list_a = [('국어', 100), ('영어', 95), ('수학', 88)]

print(sorted(list_a))   #국어, 영어, 수학 이 가나다순으로 정렬됨.
print (sorted(list_a, key=lambda data : data[1]))  
#▲ key는 정렬 기준을 정하는 역할
#▲ lambda에서 매개변수 data는 list_a의 데이터

print ("======dict====정렬==============")
dict_1 = {'국어':100, '영어':95, '수학': 88}
print(sorted(dict_1.items()))            #key 기준 가나다순으로 정렬
print(dict(sorted(dict_1.items())))      #key 기준 가나다 순으로 정렬되면서 dict 형태로 출력
print(dict(sorted(dict_1.items(), key=lambda data : data[1])))    #value 기준으로 정렬되면서 dict형태로 출력
print(dict(sorted(dict_1.items(), key=lambda data : data[1], reverse=True)))    
