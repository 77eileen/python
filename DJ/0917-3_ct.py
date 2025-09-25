# 문제 설명
# 문자열 my_string, overwrite_string과 정수 s가 주어집니다.
# 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 
# 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

# 입출력 예 설명
# 입출력 예 #1
# 예제 1번의 my_string에서 인덱스 2부터 
# overwrite_string의 길이만큼에 해당하는 부분은 "11oWor1"이고 
# 이를 "lloWorl"로 바꾼 "HelloWorld"를 return 합니다.

# 입출력 예 #2
# 예제 2번의 my_string에서 인덱스 7부터 overwrite_string의 길이만큼에 해당하는 부분은
# "29b8UYP"이고 이를 "merS123"로 바꾼 "ProgrammerS123"를 return 합니다.


def solution(my_string, overwrite_string, s):
    return (my_string[:s]+overwrite_string+my_string[s+len(overwrite_string):])

s1 = solution("He11oWor1d", "lloWorl", 2)
print(s1)


