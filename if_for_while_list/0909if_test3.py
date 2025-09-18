#명령어는 모두 실행
#조건물을 이용하면 특정 명령문은 실행되지 않게 할 수 있다.
#조건문은
#if 조건 : 
#   (들여쓰기) 해서 if에 하위 명령어로 만든다 ---> 블럭
age=20
if age >= 18:
    print ('성인입니다')
    print ('조건문은 True 입니다')
    # 기타 여러 코드 가능
    # 기타 여러 코드 가능
print('if와 상관없는 실행문')    

print('==========')

#조건에 맞으면 합격, 그렇지 않으면 불합격
score = 80
if score >=60:
    print ('합격')
print('불합격')

print('==========')

score = 40
if score >=60:
    print ('합격')
else:
    print('불합격')

print('==========')

temperature=15
if temperature > 30:
    print('덥다')
elif temperature >20:  #자바에서는 else if 로 기재
    print('따뜻하다')
elif temperature >10:  
    print('시원하다')
else:
    print('춥다')
    
