# 선거시스템
# 유권자들은 기호로 투표를 진행, 결과를 리스트에 저장
# ex) 1,2,3
# 투표는 순환문을 이용해서 유권자가 10명이라면 10번 순환하면서 후보자 (1~5) 선택
# [1,1,1,2,3,4,5,1,5]
# 리스트에 있는 각 번호의 횟수를 구해서 당선자를 출력
candidate = ["홍길동", "이순신", "강감찬", "율곡", "신사임당"]
vote = []    #투표리스트
counts = 10  #유권자10명
#input('1~5번 후보자들 중 투표를 하세요 : ')
result = {}  #투표카운트
# for _ in range(counts):
#     vote.append(int(input('투표하세요(1~5):')))
vote = [1,2,3,4,5,5,2,1,2,5]  #===> 위에 input 10개 하기 귀찮, 예시로 되는지 확인을 위해 기재해둠.
print(f'vote = {vote}')
# 
for i in vote :   #투표용지
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(f'result = {result}')

print(max(result))   #max => 가장 큰 값을 찾아내줌. max(result)로만 쓰면 딕셔너리에서 key중 가장 큰 값 출력

#key의 value를 가져올 때
#  ; 딕셔너리변수['key']  => 없으면 에러를 발생
#  ; 딕셔너리변수.get('key')  => 없어도 에러를 발생하지는 않음

# print(result.get(20))    #key 20의 value가 없으면 none으로 출력
# print(result.get(20,1))  #key 20의 value가 없으면 1로 출력

max_key = max(result, key=result.get)   #이렇게 하면 key=result.get => value로 해석, value에서 가장 큰 값 출력됨.
print (f'당선자: {candidate[max_key-1]} 득표수: {result[max_key]}')
