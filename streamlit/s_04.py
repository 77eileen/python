#차트 만들기 (시각화)
#1~100 데이터 
import random
datas=[random.randint(1,100) for i in range(10)]
print(datas)

import streamlit as st
st.write('막대 그래프')
st.bar_chart(datas)

st.write('선 그래프')
st.line_chart(datas)

st.write('영역 그래프')
st.area_chart(datas)

st.write('1X2 layout')
col1, col2 = st.columns(2)
col1.write('막대그래프')      #하기처럼 with로 해도 되고, 이것처럼 작성해도됨.
col1.bar_chart(datas)

with col2:                   # col2.line_chart(datas) 과 동일함.
    st.write('선그래프')                  
    st.line_chart(datas)   


st.write('2X2 layout')
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col1.bar_chart(datas)
col2.line_chart(datas)
col3.area_chart(datas)
col4.table(datas)


#streamlit run .\streamlit\s_04.py
