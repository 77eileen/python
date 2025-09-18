# 딕셔너리의 성질을 이용한 리스트의 요소를 카운트
# max함수를 이용해서 기준을 value로 바꿔서 가장 큰 value에 해당하는 key
# 매소드  .get()  사용

print ("===== key value==============")
# key를 이용해서 value를 가져오는 방법
dict_1 = {'사과': 10, '바나나':20}
# 포도의 value를 확인
print (dict_1['바나나'])  #인덱스 방식 : 없으면 keyerror로 출력
print (dict_1.get('바나나')) #매소드 방식
print (dict_1.get('파인애플'))  #매소드 방식: 없으면 none으로 출력
print (dict_1.get('파인애플', 10))  #매소드 방식 : 없으면, 10으로 출력


print ("====== max ================")
# 자료구조에서 가장 큰 값을 찾는 내장함수 max
print (max([1,5,2,4,8,9,1,4]))
print (max(dict_1))    #key 값 중에서 가장 큰 값이 출력 (한글에도 값이주어짐.. 그래서 에러가 안나고 출력됨)
print (max(dict_1, key=dict_1.get))


print ("====== 정렬 ================")
# 정렬 sorted() : 정렬에서 기준은 오름차순
list_1 = [5,2,1,3]
print(sorted(list_1))
print(sorted(list_1, reverse=True))
print(sorted(list_1)[::-1])


print ("====== dict 정렬 ================")
dict_1 = {'국어': 100, '국사':20, '영어': 90, '수학': 50}
print (sorted(dict_1))    #key 기준 오름차순
print (sorted(dict_1, key=dict_1.get))   #value 오름차순 기준으로 key를 정렬


