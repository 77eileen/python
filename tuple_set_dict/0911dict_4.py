
staff= {
    '홍길동' : {
        '직책' : '매니저',
        '연봉' : '2000만원',
        '경력' : {
            '삼성전자' : '5년',
            '엘지전자' : '3년',
            'sk' : '10년'
        },
        '취미': ['낚시', '헬스', '수영', '자전거']
    }
}

#엘지전자 근속연수
print(staff['홍길동']['경력']['엘지전자'])
#취미 중 자전거 출력
print(staff['홍길동']['취미'][-1])
#취미 중 독서라는 취미가 있는지 없는지 판단하려면
if '독서' in staff['홍길동']['취미']:
    print ('독서는 홍길동의 취미입니다.')
else:
    print ('독서는 홍길동의 취미가 아닙니다.')

'''
학생이 가지는 과목이 3과목이고 국어, 영어, 수학의 점수를 관리
student1 = [100, 80, 95]
student2 = [90, 85, 90]      
▲ 상기처럼 리스트로 만들면 어느과목의 어느점수인지 알수 없음.
student3 = {'국어': 100, '영어':100, '수학':80}
student4 = {'영어': 80, '국어':50, '수학':80}
student5 = {'수학': 90, '영어':100, '국어':80}
▲ 딕셔너리로 만들면 순서가 바뀌어도 해당과목의 점수를 알 수 있음.
element_class = [student3, student4, student5]
'''

student3 = {'국어': 100, '영어':75, '수학':80}
student4 = {'영어': 80, '국어':50, '수학':50}
student5 = {'수학': 90, '영어':95, '국어':70}
element_class = [student3, student4, student5]

math_score=0
for student in element_class:
    math_score += student['수학']
print (f'학생들의 수학 총점은 {math_score}')

math_list =[]
for student in element_class:
    math_list.append(student)
print(math_list)

