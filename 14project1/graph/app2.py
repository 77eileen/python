import streamlit as st
import pandas as pd
import pymysql
import plotly.express as px

# -------------------------------
# DB에서 데이터 불러오기 함수
# -------------------------------
def load_data():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root1234",
        database="prj1",
        charset="utf8mb4"
    )

    query = """
    SELECT 
        m.year,
        m.amount,
        f.fuel_name,
        c.cartype_name
    FROM main_tbl_rawdata m
    JOIN fuel_tbl f ON m.fuel_tbl_fuel_id = f.fuel_id
    JOIN cartype_tbl c ON m.cartype_tbl_cartype_id = c.cartype_id;
    """

    df = pd.read_sql(query, conn)
    conn.close()
    return df


# -------------------------------
# Streamlit 페이지 구성
# -------------------------------
st.set_page_config(page_title="연료별 차량 데이터", layout="wide")

# 메인 제목
st.title("🚗 연료별 차량 데이터")

# 사이드바 메뉴
menu = st.sidebar.radio("메뉴 선택", ["연료별 차량 현황", "FAQ"])



# -------------------------------
# Streamlit 페이지
# -------------------------------

if menu == "연료별 차량 현황":
    st.subheader("📊 연료별 차량 현황")

    df = load_data()

    # ---------------------------
    # 선택 옵션
    # ---------------------------
    fuel_order = ["휘발유", "경유", "LPG", "전기", "CNG", "하이브리드", "수소", "기타"]
    fuel_options = ["전체"] + fuel_order
    fuel_choice = st.radio("연료 종류 선택", fuel_options, horizontal=True)

    cartype_options = ["전체"] + df["cartype_name"].unique().tolist()
    cartype_choice = st.radio("차종 선택", cartype_options, horizontal=True)

    # ---------------------------
    # 데이터 필터링
    # ---------------------------
    filtered_df = df.copy()

    if fuel_choice != "전체":
        filtered_df = filtered_df[filtered_df["fuel_name"] == fuel_choice]

    if cartype_choice != "전체":
        filtered_df = filtered_df[filtered_df["cartype_name"] == cartype_choice]

    # ---------------------------
    # 그래프 그리기 (Plotly)
    # ---------------------------
    filtered_df["year"] = filtered_df["year"].astype(int)

    # fuel_name 순서 고정
    filtered_df["fuel_name"] = pd.Categorical(
        filtered_df["fuel_name"], categories=fuel_order, ordered=True
    )

    grouped = filtered_df.groupby(["year", "fuel_name"])["amount"].sum().reset_index()

    year_range = list(range(2015, 2025))  # 2015~2024

    fig = px.line(
        grouped,
        x="year",
        y="amount",
        color="fuel_name",
        markers=True,
        category_orders={"fuel_name": fuel_order, "year": year_range},
        labels={"year": "연도", "amount": "차량 수", "fuel_name": "연료 종류"},
        title="연료별 차량 등록 현황"
    )

    fig.update_layout(
        xaxis=dict(tickmode="linear", tick0=2015, dtick=1),
        yaxis=dict(tickformat="d"),
        legend_title_text="연료 종류",
        font=dict(family="Malgun Gothic")  # 한글 깨짐 방지
    )

    st.plotly_chart(fig, use_container_width=True)