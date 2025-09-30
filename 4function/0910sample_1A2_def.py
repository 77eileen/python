# 가위,바위,보 게임 (컴퓨터vs휴먼)
# 가위 1, 바위:2, 보:3
# 규칙: 컴퓨터가 임의로 숫자를 선택  : random
# 인간이 숫자를 입력                : input
# 승패를 기록                       
# 3번마다 계속할지 물어본다          : for 


#개발
#1. 요구사항 전달 받아서 분석서를 작성
#2. 기술조사 (ex. random, input 등)


#가위 1, 바위:2, 보:3 
import random

def get_com_num(start=1, end=3):
    ''' 랜덤값 출력 (start~end)'''
    return random.randint(start,end)


def get_human_num():
    return int(input('가위 1, 바위:2, 보:3 중에서 하나의 숫자를 입력하세요 : '))

def check_winner(com_choice, human_choice):
    if com_choice == human_choice:
        print('비겼습니다.')
    else: 
        if (com_choice==1 and human_choice ==2 ) or \
        (com_choice==2 and human_choice ==3 ) or \
        (com_choice==3 and human_choice ==1 ) :
            print ('당신이 이겼습니다.')
        else : 
            print ('당신이 졌습니다.')

#랜덤하게 선택한 컴퓨터 값   
com_choice = get_com_num()
print(f'랜덤 컴퓨터값 : {com_choice}')  #디버깅용으로 개발이 완료되면 삭제 또는 비공개 


#사용자값 
human_choice = get_human_num()

#승패
check_winner(com_choice, human_choice)

