import time

#함수1 만들기
def display_second(count):
    count += 1                    #함수안에서 정의할 수 없는 변수는 받아와야함. 함수안에 count=0을만들면 항상 0으로 초기화되므로, 여기 함수 안에서 count=0으로 선언하지말고, 이 함수 밖에서 count=0 선언.
    print(f'{count}초')
    time.sleep(1)   # 1초간 지연
    return count


#함수2. 5초단위로 사용자한테 계속 할건지 물어본다.. "To be Continue(Y/y)"
def is_user_continue(count):
    if count % 5 ==0 : 
        user_input = input('To be continue (y/Y)').upper()
        if not user_input == "Y":     #====> if user_input != "Y": 같은 표현
            return False
    else:                           
        return True
    #==> 아래쪽 if로 들여쓰기 되어 있으면 
    #    나누기 5일 때 0이 안되면 다시 True로 넘어가서 계속 5초 될때까지 돌아야 하는데, 
    #    아래쪽 if로 들여쓰기 되어 있으면 if not user input Y가 아닐때 else가 작동되므로,
    #    위쪽 if와 같은 열에 작성되어야함.



is_continue = True
count = 0
while is_continue:
    count = display_second(count)     #1초간격으로 출력
    is_continue = is_user_continue(count)

#VScode 에서 디버깅을 제공
#26열에 break point 잡아두고 (빨간점)
#python디버거 : python 파일 디버거 실행
#F10 눌러서 하나씩 단계로 실행하다보면,
#count = 1 이후 실행하면 while is_contiune: 와 is_user_continue(count)가 none으로 뜸.
#그럼 디버깅 멈추고, 다시 디버깅을 처음부터 실행해서 
#count =1 일 때 is_continue= is_user_continue(count) 열에서 F11눌러서 해당 함수에 들어가서
#왜 none이 되었는지 파악할것.
#그럼 count가 5가 아닐때(5초 아닐때) 계속 진행되는 else True가 안되므로 오류가 난것을 확인해서 다시 수정하기.

