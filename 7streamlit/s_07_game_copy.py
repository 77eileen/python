import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(
    page_title="GAME",
    layout="wide"  # 전체 페이지를 wide 모드로 설정
)

# 사이드바 메뉴 생성
with st.sidebar:
    st.title("메뉴")
    selected_menu = st.radio(
        "원하시는 메뉴를 선택하세요:",
        ["숫자 맞추기", "가위, 바위, 보", "설정", "도움말"]
    )

# 메인 컨텐츠 영역
def guess_num_play():
    st.header("숫자 맞추기")
    st.write("컴퓨터의 숫자를 맞춰보세요!")
    # 컴퓨터가 랜덤 숫자 선택
    if 'c_num' not in st.session_state:   
        st.session_state['c_num'] = random.randint(1,100)  #st.session_state['c_num'] 같음 st.session_state.c_num
    c_num = st.session_state.c_num
    # 사용자로 부터 숫자 입력 1~100 사이
    # number_input 위젯에서 엔터키가 입력되었을 때 값을 리턴해서 h_num 에 저장
    h_num=st.number_input('1~100사이 숫자 입력하고 enter키를 눌러주세요', 1,100, key='h_num')  
    h_num=st.session_state.h_num
    
    if c_num > h_num:
        st.warning('사용자가 입력한 값이 더 작아요!')
        
    elif c_num < h_num:
        st.warning('사용자가 입력한 값이 더 커요!')
    else:
        st.success(f'정답입니다👍 {c_num}')
        st.balloons()   #축하 애니메이션
        del st.session_state.c_num





# def r_p_s_play():
#     st.header("가위, 바위, 보")
#     st.write("컴퓨터와 가위, 바위, 보 게임에서 승리하세요!")
#     # 컴퓨터가 랜덤 숫자 선택
#     if 'com_choice' not in st.session_state:   
#         st.session_state['com_choice'] = random.randint(1,3)  #st.session_state['c_num'] 같음 st.session_state.c_num
#     com_choice = st.session_state.com_choice
#     # 사용자로 부터 가위, 바위, 보 입력
#     with st.container(horizontal=True, 
#                   gap="medium", 
#                   border=True
#                   ):   #horizontal=True 가로 정렬 False 세로 정렬
#      st.button('가위')
#      st.button('바위')
#      st.button('보')






class RPSGame:
    def __init__ (self):
        self.choices = {1: '가위', 2: '바위', 3: '보'}
    
    def get_computer_choice (self):
        if 'com_choice' not in st.session_state:   
             st.session_state['com_choice'] = random.randint(1,3)  #st.session_state['c_num'] 같음 st.session_state.c_num
    com_choice = st.session_state.com_choice
    
    def get_user_choice (self):
        try:
            user_choice=st.number_input("가위(1), 바위(2), 보(3) 중 하나를 선택하세요: ", 1,3, key='user_choice')
            user_choice=st.session_state.user_choice
            if user_choice in self.choices:
                return user_choice
            else:
                print("잘못된 입력입니다. 1, 2, 3 중 하나를 선택하세요.")
        except ValueError:
            print("숫자를 입력하세요.")

    def determine_winner (self, user, computer):
        if user == computer:
            return "비겼습니다!"
        elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
            return "사용자가 이겼습니다!"
        else:
            return "컴퓨터가 이겼습니다!"
    
    def play (self):
        st.button('play')
        # while True:
        user_choice = self.get_user_choice()
        com_choice = self.get_computer_choice()
        st.warning (f"사용자 선택: {self.choices[user_choice]}, 컴퓨터 선택: {self.choices[com_choice]}")
              
            # again = input("다시 하시겠습니까? (y/n): ").strip().lower()
            # if again != 'y':
            #     print("게임을 종료합니다.")
            #     break       
while True:
    RPSGame().play()    #객체를 만들어서 변수로 저장할 필요가 없음. 아까 학생 class 만들 때 처럼 이름, 과목  등 이런걸 입력할게 아니므로.. 
    #RPSGame().play().   #play(). def play 함수 안에 것을 (return) 호출할 수도 있음.
    again = st.text_input("다시 하시겠습니까? (y/n): ").strip().lower() #strip() : 앞뒤 공백 제거, lower() : 소문자로 변환
    if again != 'y':
        print("게임을 종료합니다.")
        break 

























    
def show_settings():
    st.header("설정")
    st.text_input("사용자 이름")

    
def show_help():
    st.header("도움말")
    st.write("도움이 필요하시다면 아래 연락처로 문의해주세요:")
    st.write("이메일: help@example.com")

# 선택된 메뉴에 따라 해당하는 컨텐츠 표시
if selected_menu == "숫자 맞추기":
    guess_num_play()
elif selected_menu == "가위, 바위, 보":
    RPSGame().play()
elif selected_menu == "설정":
    show_settings()
elif selected_menu == "도움말":
    show_help()




#streamlit run .\streamlit\s_07_game_copy.py
