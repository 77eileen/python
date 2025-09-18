# pip install streamlit - 터미널에서 실행
import streamlit as st
st.title('타이틀')
st.header('헤더')
st.subheader('서브헤더')
st.write('앱')
st.button('버튼')
st.checkbox('체크박스')
st.radio('레디오박스',('a','b','c'))   #레디오박스는 옵션 선택사항이므로 옵션을 만들어줘야함.
st.selectbox('셀렉트 박스', (1,2,3,4,5,6))
st.slider('슬라이더',0,100,50)  #('슬라이더',최대,최소,기본값)
st.text_input('텍스트 상자')
#st.video 
#st.image

# name = st.text_input('이름을 입력하세요')
# st.write(f'안녕하세요 {name}님!!')

# 터미널에 하기 실행시키기
# streamlit run ./streamlit/s_01.py  (경로: streamlit/s_01.py)
# 실행안되는 경우, 경로 확인해보기 (경로복사 / 상대경로복사 넣어서 하기)
# 계속 진행되고 있으므로, 여기서 변경 후 저장하고 윈도우창 새로고침 하면 반영됨.
#  Ctrl + C 터미널에서 눌러서 진행 멈춰주기
# streamlit 은 반응형으로 윈도우 창 변형에 따라서 알아서 조절됨.
