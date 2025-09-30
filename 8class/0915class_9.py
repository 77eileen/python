# 가위 바위 보 게임을 클래스로 구현하기
# 사용자는 '가위', '바위', '보' 입력
# 컴퓨터 무작위 선택
# 게임의 승패를 판단하고 결과를 출력
# 가위는 1, 바위는 2, 보는 3으로 표현
# 게임이 끝나면 계속할지 물어본다

import random
class RPSGame:
    def __init__ (self):
        self.choices = {1: '가위', 2: '바위', 3: '보'}
    
    def get_computer_choice (self):
        return random.randint(1, 3)
    
    def get_user_choice (self):
        while True:
            try:
                user_input = int(input("가위(1), 바위(2), 보(3) 중 하나를 선택하세요: "))
                if user_input in self.choices:
                    return user_input
                else:
                    print("잘못된 입력입니다. 1, 2, 3 중 하나를 선택하세요.")
            except ValueError:
                print("숫자를 입력하세요.")
    
    def determine_winner (self, user, computer):
        if user == computer:
            return "비겼습니다!"
        elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
            return "사용자가 이겼습니다!"
        else:
            return "컴퓨터가 이겼습니다!"
    
    def play (self):
        # while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(f"사용자 선택: {self.choices[user_choice]}, 컴퓨터 선택: {self.choices[computer_choice]}")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)
            
            # again = input("다시 하시겠습니까? (y/n): ").strip().lower()
            # if again != 'y':
            #     print("게임을 종료합니다.")
            #     break       
while True:
    RPSGame().play()    #객체를 만들어서 변수로 저장할 필요가 없음. 아까 학생 class 만들 때 처럼 이름, 과목  등 이런걸 입력할게 아니므로.. 
    #RPSGame().play().   #play(). def play 함수 안에 것을 (return) 호출할 수도 있음.
    again = input("다시 하시겠습니까? (y/n): ").strip().lower() #strip() : 앞뒤 공백 제거, lower() : 소문자로 변환
    if again != 'y':
        print("게임을 종료합니다.")
        break 
