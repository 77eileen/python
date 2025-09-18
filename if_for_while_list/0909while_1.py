# while문은 반복횟수가 없다.
# while 조건:

count = 0
while count < 10 :  #이런건 순환문 횟수가 정해져있으므로 for문 사용하도록. while은 갯수가 아니라 조건이 만족할때까지 무한 돌때 사용 (ex. 에어컨 일정온도로 무한 순환으로 유지되게.)
    print (f'순환문 : {count}') #상기 count < 10 으로 안정하면 무한정 순환됨.
    count += 1


#예제 : 답1
import time

count = 0
while True:
    count += 1
    print(f'{count}초')
    time.sleep(1)   #sleep(1) 1초간 지연
    
    #5초 단위로 사용자한테 계속 할건지 물어본다. "to be continue(Y/y)"
    if count % 5 ==0 : 
        is_continue = input('To be continue (y/Y)')
        #사용자의 모든 입력치를 대문자로 바꿔주는 코딩
        #is_continue = is_continue.upper()
        #if is_continue == "Y": 로하면 하기 문장 대체 가능
        if is_continue == "Y" or is_continue == "y":
            pass
        else:
            break

        #if not is_continue == "Y":
            #break
        #if is_continue != "Y":
            #break
print ("종료")

