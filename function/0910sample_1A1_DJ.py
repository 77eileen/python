# 가위,바위,보 게임 (컴퓨터vs휴먼)
# 가위 1, 바위:2, 보:3
# 규칙: 컴퓨터가 임의로 숫자를 선택  : random
# 인간이 숫자를 입력                : input
# 승패를 기록                       
# 3번마다 계속할지 물어본다          : for 


#개발
#1. 요구사항 전달 받아서 분석서를 작성
#2. 기술조사 (ex. random, input 등)

#ref. randint (1,3) 에서 3까지 선택되는지 확인해보는 코딩
# import random
# for i in range (100):
#     if random.randint(1,3) ==3:
#         print ('성공')
#         break



import random
#가위 1, 바위:2, 보:3 
#랜덤하게 선택한 컴퓨터 값

for i in range (100):
    com_choice = random.randint (1,3)
    print(f'com_choice : {com_choice}')  #디버깅용으로 개발이 완료되면 삭제 또는 비공개 
    #사용자값
    human_choice = int(input('가위 1, 바위:2, 보:3 중에서 하나의 숫자를 입력하세요 : '))
    #승패 확인
    if com_choice==1:
        if human_choice==1:
            print ('무승부')
        elif human_choice ==2:
            print ('인간승리')
        elif human_choice ==3:
            print ('컴퓨터 승리')
    elif com_choice==2:
        if human_choice==2:
            print ('무승부')
        elif human_choice ==3:
            print ('인간승리')
        elif human_choice ==1:
            print ('컴퓨터 승리')
    elif com_choice==3:
        if human_choice==3:
            print ('무승부')
        elif human_choice ==1:
            print ('인간승리')
        elif human_choice ==2:
            print ('컴퓨터 승리')
            if i%3==0:
                user_continue = input('계속 진행하시겠습니까? (Y/N)')
                if user_continue == 'Y' :
                    pass
                else:
                    break