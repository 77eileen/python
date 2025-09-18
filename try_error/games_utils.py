
# #1~100사이 정수를 입력하는 방법에 대한 로직.
# while True:
#     try:
#         h_num = int(input('1~100 사이 정수를 입력하세요'))
#         if not 0 <= h_num <= 100:
#             raise ValueError('1~100 사이 범위 초과')
#         #break    #break1 여기도 가능하고
#     except Exception as e:
#         print (f'오류발생 {e} {e.__class__.__name__}')
#     else:
#         break    #else break2 로도 가능

# 상기 로직을 함수로 만들어보세요.
# 사용자 입력 처리 함수
# 이름 get_data()
# parameter
    #start: 시작값
    #end : 종료값
    #input_str : 가이드 문구 
# 사용자 입력은 input()
# return 정수로 변환된 입력값
# 상기 로직을 함수로 만들어보세요.
def get_data(start, end, input_str="정수"):
    while True:
        try:
            h_num = int(input(f'{start}~{end}의 {input_str}입력 : '))
            if not int(start) <= h_num <= int(end):
                raise ValueError(f'{start} ~ {end} 사이 범위 초과')
        except Exception as e:
            print (f'오류발생 {e} {e.__class__.__name__}')
        else:
            return h_num    #상기 참조. break 부분에 return 으로 가능? 

#승자 선택 로직 함수
#게임
#human > computer : 크다
#human < computer : 작다
#human = computer : 정답
def check_winner(human, com_num, game_history, count):
    if human > com_num:
        print (f'human > computer : 크다')
        game_history.append ((human,'크다'))
    elif human < com_num : 
        print (f'human < computer : 작다')
        game_history.append ((human, '작다'))
    else:
        print(f'정답 {com_num}. 시도 횟수 : {count}') 
        for guess_value, state in game_history:
            print (f' 사용자 입력값 {guess_value} - {state} ')
        return True
    return False