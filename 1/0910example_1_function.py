# 가위,바위,보 게임 (컴퓨터vs휴먼)
# 가위 1, 바위:2, 보:3
# 규칙: 컴퓨터가 임의로 숫자를 선택  : random
# 인간이 숫자를 입력                : input
# 승패를 기록                       
# 3번마다 계속할지 물어본다          : for 


import games

for i in range(1,101):
    if i % 3 == 0 :
        is_continue = input('계속 진행하시겠습니까? (Y/N)')
        if not is_continue == 'Y' :
            break
    #랜덤하게 선택한 컴퓨터 값   
    com_choice = games.get_com_num()
    print (f'랜덤 값 확인 {com_choice}') #디버깅 확인
    
    #사용자값 
    human_choice = games.get_human_num()

    #승패
    games.check_winner(com_choice, human_choice)

                