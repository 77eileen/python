print ("======= map1 ==============")
# map : 자료구조의 각 요소에 특정 함수를 적용
str_numbers = ['1', '10', '100']
print(str_numbers)             #문자로 출력
print(map(int, str_numbers))   #map 객체다. 라고만 출력
print (list(map(int, str_numbers)))   #각 요소를 int로 바꿔서 출력됨


print ("======= map split ==============")
scores = input ('국어 영어 수학 점수를 공백을 기준으로 입력하세요 : ')
scores = scores.split ()      #split () ()공백을 기준으로 문자열을 잘라서 list로 저장
print (scores)
kor, eng, math = map(int, scores)
print(kor+eng+math)

print ("======= map lambda ==============")
list_2=[10,20,30]
#각 원소에 2를 곱한다
def test (data) : 
    return data*2
print (list(map (test, list_2)))
#상기 test 함수 대신 lambda 사용
print (list(map (lambda data: data*2, list_2)))
