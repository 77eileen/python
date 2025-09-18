import streamlit as st
import random

# 컴퓨터가 랜덤 숫자 선택
if 'c_num' not in st.session_state:   
    st.session_state['c_num'] = random.randint(1,100)  #st.session_state['c_num'] 같음 st.session_state.c_num
c_num = st.session_state.c_num
# 사용자로 부터 숫자 입력 1~100 사이
h_num=st.number_input('1~100사이 숫자 입력', 1,100)   #text_input은 텍스트 입력이고, number_input은 숫자로 한정해줌. 숫자범위기재.

 
if st.button ('결과 확인'):
    # st.write('컴퓨터 숫자', c_num)   #확인용.. 컴퓨터가 계속 값을 변경함.
    if c_num > h_num:
        st.write('다운 : 사용자가 입력한 값이 더 작다')
    elif c_num < h_num:
        st.write('업 : 사용자가 입력한 값이 더 크다')
    else:
        st.write('컴퓨터 숫자:', c_num)
        st.write('정답')
        st.balloons()   #축하 애니메이션

#서버가 무한으로 계속 돌고 있으므로 순환문 만들필요 없음.

#streamlit run .\streamlit\s_02.py