# 문자들이 담겨있는 배열 arr가 주어집니다. arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요.
def solution(arr):
    for i in range(len(arr)):
     answer = arr[i:len(arr)]
    return answer

s1 = solution('hir')
print(s1)


def solution(arr):
    answer = ""  # 먼저 빈 문자열을 준비
    for char in arr:  # 배열 arr의 각 원소(char)를 하나씩 꺼내서
        answer += char  # answer에 이어 붙인다
    return answer

# 테스트
s1 = solution('hir')
print(s1)  # 출력: hir



# 문자열 my_string과 정수 k가 주어질 때,
# my_string을 k번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution_1(my_string, k):
    answer = my_string*k
    return answer

s2 = solution_1('love', 3)
print(s2)


# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
# 12 ⊕ 3 = 123
# 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, 
# a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.
# 단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.

def solution2(a, b):
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    if int(ab) >= int (ba):
        return ab
    else:
        return ba

s3 = solution2(23,7)
print(s3)


# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
# 12 ⊕ 3 = 123
# 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, 
# a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.
# 단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.

def solution4(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    if int(ab) >= 2*a*b:
        return (int(ab))
    else:
        return (2*a*b)
    
s4 = solution4(91,2)
print(s4)


# 정수 num과 n이 매개 변수로 주어질 때, 
# num이 n의 배수이면 1을 return 
# n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.

def solution5(num, n):
    if num % n == 0:
        return (1)
    else:
        return (0)
    
s5 = solution5(92, 2)
print(s5)