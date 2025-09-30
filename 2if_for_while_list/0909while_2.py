#예제: 답2
import time

count = 0
is_continue = True
while is_continue:
    count += 1
    print(f'{count}초')
    time.sleep(1)   #sleep(1) 1초간 지연
    
    #5초 단위로 사용자한테 계속 할건지 물어본다. "to be continue(Y/y)"
    if count % 5 ==0 : 
        user_input = input('To be continue (y/Y)').upper()
        if not user_input == "Y":     #====> if user_input != "Y": 같은 표현
            is_continue = False
