# 사용자로부터 점수를 입력받아서 A B C D F 학점을 출력
score = int(input('총점을 입력하세요: '))
print(f'입력된 score 는 {score}')

if score >= 90:    
    print('A')     #90점 이상 : A
elif score >= 80:
    print('B')     #80~89 : B
elif score >= 70:
    print('C')     #70~79 : C
elif score >= 60:
    print('D')     #60~69 : D
else:
    print('F')     #~60 : F