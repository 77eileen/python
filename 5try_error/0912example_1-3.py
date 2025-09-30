# 숫자 맞추기 게임
# 1~100사이에 임의의 숫자를 컴퓨터가 선택. 
# 사용자가 숫자 선택
# 숫자에 따라 정답 / 사용자가 선택한 숫자보다  up / 사용자가 선택한 숫자보다 down 

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



#컴퓨터가 선택한 랜덤 정수
import random as rd
start, end = 1, 100    #tuple 형태로 파이썬에서 자동으로 바꿔줌. start, end = (1,100)
com_num = rd.randint(start, end)

#게임
#human > computer : 크다
#human < computer : 작다
#human = computer : 정답
count = 0
game_history =[]
while True:
    human = get_data(start, end)
    count += 1
    #게임
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
        break


#내가 몇번만에 맞췄는지 counting 해보기
#너가 이런 과정을 거쳐서 정답을 맞춘것에 대한 히스토리 레포트를 출력해보기.


