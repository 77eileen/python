# 숫자 맞추기 게임
# 1~100사이에 임의의 숫자를 컴퓨터가 선택. 
# 사용자가 숫자 선택
# 숫자에 따라 정답 / 사용자가 선택한 숫자보다  up / 사용자가 선택한 숫자보다 down 

#1~100사이 정수를 입력하는 방법에 대한 로직.
# for i in range(10): 
while True:
    try:
        h_num = int(input('1~100 사이 정수를 입력하세요'))
        if not 0 <= h_num <= 100:
            raise ValueError('1~100 사이 범위 초과')
        #break    #break1 여기도 가능하고
    except Exception as e:
        print (f'오류발생 {e} {e.__class__.__name__}')
    else:
        break    #else break2 로도 가능
    #break3 여기도 가능하나 상기 break1,2가 더 나음.


# 사용자 입력 처리 함수
# 이름 get_data()
# parameter
    #start: 시작값
    #end : 종료값
    #input_str : 가이드 문구 
# 사용자 입력은 input()
# return 정수로 변환된 입력값

