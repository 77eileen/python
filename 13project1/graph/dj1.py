import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# -------------------------------
# 1. MySQL 연결
# -------------------------------
# # 예시: mysql+pymysql://user:password@host:port/dbname
engine = create_engine("mysql+pymysql://root:root1234@127.0.0.1:3306/prj1")


# import pymysql 
# from dotenv import load_dotenv
# import os

# #.env로드
# load_dotenv()

# #1. DB연결
# conn=pymysql.connect(
#     host=os.getenv('DB_HOST'),
#     user=os.getenv('DB_USER'),
#     password=os.getenv('DB_PASSWORD'),
#     database=os.getenv('DB_NAME'))

# print('접속성공')



# -------------------------------
# 2. 데이터 불러오기 (조인)
# -------------------------------
query = """
SELECT 
    m.year,
    m.mount AS amount,
    f.fuel_name,
    c.cartype_name
FROM main_tbl_rawdata m
JOIN fuel_tbl f ON m.fuel_tbl_fuel_id = f.fuel_id
JOIN cartype_tbl c ON m.cartype_tbl_cartype_id = c.cartype_id
WHERE m.year BETWEEN 2015 AND 2024
"""
df = pd.read_sql(query, engine)

# -------------------------------
# 3. Streamlit UI
# -------------------------------
st.title("차량 등록 현황 (2015~2024)")

# 연료 선택 (기본 전체 선택)
fuel_options = df["fuel_name"].unique().tolist()
selected_fuels = st.multiselect("연료 선택", fuel_options, default=fuel_options)

# 차종 선택 (기본 전체 선택)
cartype_options = df["cartype_name"].unique().tolist()
selected_cartypes = st.multiselect("차종 선택", cartype_options, default=cartype_options)

# -------------------------------
# 4. 필터링
# -------------------------------
filtered_df = df[
    (df["fuel_name"].isin(selected_fuels)) &
    (df["cartype_name"].isin(selected_cartypes))
]

# -------------------------------
# 5. 집계 (연도별 합계)
# -------------------------------
summary = filtered_df.groupby("year")["amount"].sum().reset_index()

# -------------------------------
# 6. 그래프 출력
# -------------------------------
fig, ax = plt.subplots()
ax.plot(summary["year"], summary["amount"], marker="o", label="차량 수")
ax.set_xlabel("연도")
ax.set_ylabel("차량 수")
ax.set_title("연도별 차량 등록 현황")
ax.legend()

st.pyplot(fig)
