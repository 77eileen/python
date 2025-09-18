# session 개념
# 각각의 사용자를 구분하기 위한 key
# 딕셔너리
# 세션을 사용한다는 것은 값을 유지한다는 것

import streamlit as st
if 'count' not in st.session_state:   
    st.session_state.count=0        #딕셔너리에 key를 생성해준다고 보면 됨.
if st.button('카운트 증가'):
    st.write('버튼 클릭됨')
    st.session_state.count += 1    #st.session_state['count'] +=1 도 동일
st.write('현재카운트: ', st.session_state.count)   #카운트 증가 버튼을 눌러도 카운트가 +1 증가되지 않고, 버튼을 누르면 해당페이지를 다시 요청하는 것으로 인식함.(버튼을 누르면 다시 0부터 시작.. 새로고침처럼..) 그래서 증가되지 않음.
st.json(st.session_state)   #json 사용시 딕셔너리 형태로 나옴.
# session_state 사용




#streamlit run .\streamlit\s_03.py