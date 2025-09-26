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





def r_p_s_play():
    st.header("가위, 바위, 보")
    st.write("컴퓨터와 가위, 바위, 보 게임에서 승리하세요!")

    # 사용자로 부터 가위, 바위, 보 입력
    if 'user_choice' not in st.session_state:
        st.session_state.user_choice = 0
    with st.container(horizontal=True, 
                  gap="medium", 
                  border=True
                  ):   #horizontal=True 가로 정렬 False 세로 정렬
  
        
        if st.button("가위", key="btn1"):
            st.session_state.user_choice = 1
        elif st.button("바위", key="btn2"):
            st.session_state.user_choice = 2
        elif st.button("보", key="btn3"):
            st.session_state.user_choice = 3
    
    # 컴퓨터가 랜덤 숫자 선택
    if st.session_state.user_choice != 0:
        value = st.session_state.user_choice
        com_choice = random.randint(1, 3)  # 클릭 시마다 새로 선택
    
        st.write(f"컴퓨터: {['가위','바위','보'][com_choice-1]}")
        st.write(f"사용자: {['가위','바위','보'][value-1]}")

    # 승패판단
    if value == com_choice:
        st.info("무승부!")
    elif (value == 1 and com_choice == 3) or (value == 2 and com_choice == 1) or (value == 3 and com_choice == 2):
        st.success("사용자가 이겼습니다! 👍")
        st.balloons()
    else:
        st.warning("컴퓨터가 이겼습니다!")
  








    
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
    r_p_s_play()
elif selected_menu == "설정":
    show_settings()
elif selected_menu == "도움말":
    show_help()




#streamlit run .\streamlit\s_07_game.py
