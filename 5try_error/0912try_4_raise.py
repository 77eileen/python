# raise 예외를 강제로 발생시킴
print ('정상코드')
print ("예외 발생")
#raise "내가 발생시킨 오류"
    # 출력 ==> TypeError: exceptions must derive from BaseException
#raise ValueError
    # 출력 ==> ValueError
#raise ValueError("테스트")
    # 출력 ==> ValueError: 테스트 ==> 기존 에러에 내가 "테스트"라는 설명을 줄 수 있음.

print ("=====================================")
try:
    print ('정상코드')
    print ("예외 발생")
    raise "내가 발생시킨 오류"   #출력 ==> exceptions must derive from BaseException <class 'TypeError'> TypeError (ref.class로 에러 종류를 만들수 있음.)
    # raise ValueError("테스트")
except Exception as e:
    print (f'에러 : {e} {e.__class__} {e.__class__.__name__}')