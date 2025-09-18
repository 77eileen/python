# 짝수홀수 맞추기 게임
# 컴퓨터가 1~10 사이 숫자를 랜덤으로 뽑습니다.
# 사용자가 "짝" 또는 "홀"을 입력합니다.
# 맞추면 "정답!", 틀리면 "오답!".
# class OddEvenGame으로 작성하세요.

import random

class OddEvenGame():
    choices = {1 : "홀", 2: "짝"}

    def __init__ (self):
        self.com_num = None
        self.user_num = None
    def get_com_num (self):
        self.com_num = int(random.randint(1,10))
    def get_user_num (self):
        while True:
            try:
                self.user_num=int(input ('홀(1) or 짝(2) 중에서 선택하세요 :  '))
                if self.user_num in self.choices:
                    break
                else:
                    print ('잘 못 입력되었습니다. 홀(1), 짝(2) 에서 1,2 중 입력하세요.')
            except Exception as e:
                print("숫자를 입력하세요.")
    def check_num (self):
        if self.com_num % 2 ==0 and self.user_num ==2 :
            print ('짝수. 정답입니다.')
        elif self.com_num %2 != 0 and self.user_num ==1 :
            print ('홀수. 정답입니다.')
        else:
            print ('오답입니다.')

    def play(self):
        while True:
            self.get_com_num()
            self.get_user_num()
            self.check_num()

            again = input("다시 하시겠습니까? (Y/N) : ").strip().lower()
            if again != "y":
                print("게임을 종료합니다. 감사합니다!")
                break


g1 = OddEvenGame()
g1.play()


######################################다시해보기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


