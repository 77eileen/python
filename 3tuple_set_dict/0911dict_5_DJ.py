# 선거시스템
# 유권자들은 기호로 투표를 진행, 결과를 리스트에 저장
# ex) 1,2,3
# 투표는 순환문을 이용해서 유권자가 10명이라면 10번 순환하면서 후보자 (1~5) 선택
# [1,1,1,2,3,4,5,1,5]
# 리스트에 있는 각 번호의 횟수를 구해서 당선자를 출력
candidate = ["홍길동", "이순신", "강감찬", "율곡", "신사임당"]
vote = [] #투표리스트
counts = 10 #유권자
input('1~5번 후보자들 중 투표를 하세요 : ')

for count in range(counts):
    count_vote = int(input('1~5번 후보자들 중 투표를 하세요 : '))
    vote.append(count_vote)
print(vote)            # ===> 후보자들이 유권자를 선택

vote_result = { '1홍길동' : 0, '2이순신':0, '3강감찬':0, '4율곡':0, '5신사임당':0 }
for v in vote:
    if v==1:
        vote_result['1홍길동'] +=1
    elif v==2:
        vote_result['2이순신'] +=1
    elif v==3:
        vote_result['3강감찬'] +=1
    elif v==4:
        vote_result['4율곡'] +=1
    else:
        vote_result['5신사임당'] +=1

print(vote_result)

print(max(vote_result, key=vote_result.get))
print(max(vote_result))




        

