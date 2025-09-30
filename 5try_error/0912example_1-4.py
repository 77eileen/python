# 숫자 맞추기 게임
# 1~100사이에 임의의 숫자를 컴퓨터가 선택. 
# 사용자가 숫자 선택
# 숫자에 따라 정답 / 사용자가 선택한 숫자보다  up / 사용자가 선택한 숫자보다 down 




#컴퓨터가 선택한 랜덤 정수
import games_utils as gu
import random as rd
start, end = 1, 100    #tuple 형태로 파이썬에서 자동으로 바꿔줌. start, end = (1,100)
com_num = rd.randint(start, end)

count = 0
game_history =[]
while True:
    human = gu.get_data(start, end)
    count += 1
    #승자 선택 로직
    if gu.check_winner(human, com_num, game_history, count):
        break              #check_winner 함수가 실행되면서 마지막에 True가 되면 break롤 동작


#내가 몇번만에 맞췄는지 counting 해보기
#너가 이런 과정을 거쳐서 정답을 맞춘것에 대한 히스토리 레포트를 출력해보기.


