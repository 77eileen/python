import streamlit as st

with st.container(horizontal=True, 
                  gap="medium", 
                  border=True
                  ):   #horizontal=True 가로 정렬 False 세로 정렬
     st.button('Button 1')
     st.button('Button 2')
    # cols = st.columns(2, gap="medium", width=300)




# 참조
# https://github.com/streamlit/demo-seattle-weather/blob/main/streamlit_app.py
#streamlit run .\streamlit\s_05.py