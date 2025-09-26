#숫자맞추기 게임
#규칙
#1. 컴퓨터가 1~100 사이의 숫자를 랜덤으로 선택
#2. 사용자는 숫자를 입력하여 선택한 숫자를 맞춥니다
#3. 사용자 숫자 > 컴퓨터 숫자 : 크다
#4. 사용자 숫자 < 컴퓨터 숫자 : 작다
#5. 사용자 숫자 = 컴퓨터 숫자 : 정답
#6. 사용자 숫자 맞출 때 까지 계속 입력

import random
class NumberGuessingGame:
    def __init__(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

    def guess(self, user_guess):
        self.attempts += 1
        if user_guess < self.number_to_guess:
            return "너무 작습니다."
        elif user_guess > self.number_to_guess:
            return "너무 큽니다."
        else:
            return f"정답입니다! {self.attempts}번 만에 맞추셨습니다."

game = NumberGuessingGame()
while True:
    try:
        user_input = int(input("1부터 100 사이의 숫자를 입력하세요: "))
        if 1 <= user_input <= 100:
            result = game.guess(user_input)
            print(result)
            if result.startswith("정답입니다"):
                break
        else:
            print("1부터 100 사이의 숫자를 입력하세요.")
    except ValueError:
        print("유효한 숫자를 입력하세요.")        
        


## user_guess 를 init 에 기재하는 것과 
    # def __init__(self):
    #     self.user_guess = None
## def guess (self, user_guess)따로 정의 하는 것과 차이??????


