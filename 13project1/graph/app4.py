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
st.set_page_config(page_title="자동차 연료 등록 현황", layout="wide")

# 메인 제목
st.title("🚗 연료별 차량 데이터")

# # 사이드바 메뉴
# menu = st.sidebar.radio("메뉴 선택", ["연료별 차량 현황", "FAQ"])


# -------------------------------
# Streamlit 페이지
# -------------------------------
menu = st.sidebar.selectbox("메뉴", ["연료별 차량 현황", "연도별 연료별 순위", "FAQ"])

df = load_data()

# -------------------------------
# 1) 연료별 차량 현황
# -------------------------------
if menu == "연료별 차량 현황":
    st.subheader("📊 연료별 차량 현황")

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

    filtered_df["year"] = filtered_df["year"].astype(int)

    available_fuels = [f for f in fuel_order if f in filtered_df["fuel_name"].unique()]
    filtered_df["fuel_name"] = pd.Categorical(
        filtered_df["fuel_name"], categories=available_fuels, ordered=True
    )

    grouped = filtered_df.groupby(["year", "fuel_name"])["amount"].sum().reset_index()
    year_range = list(range(2015, 2025))  # 2015~2024

    fuel_colors = {
        "휘발유": "#FF0000", "경유": "#808080", "LPG": "#FFA500",
        "전기": "#0000FF", "CNG": "#00BFFF", "하이브리드": "#008000",
        "수소": "#800080", "기타": "#A52A2A"
    }

    fig = px.line(
        grouped,
        x="year",
        y="amount",
        color="fuel_name",
        markers=True,
        category_orders={"fuel_name": available_fuels, "year": year_range},
        color_discrete_map=fuel_colors,
        labels={"year": "연도", "amount": "차량 수", "fuel_name": "연료 종류"},
        title="연료별 차량 등록 현황"
    )

    y_max = grouped["amount"].max() * 1.5

    fig.update_layout(
        xaxis=dict(title=dict(text="연도", font=dict(size=16)), tickmode="linear", tick0=2015, dtick=1),
        yaxis=dict(title=dict(text="차량 수", font=dict(size=16)), tickformat=",d", range=[0, y_max]),
        legend_title_text="연료 종류",
        font=dict(family="Malgun Gothic"),
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# 2) 연도별 연료별 순위 막대그래프
# -------------------------------
elif menu == "연도별 연료별 순위":
    st.subheader("📊 연도별 연료별 순위")

    # ---------------------------
    # 메인에서 연도 선택
    # ---------------------------
    selected_year = st.selectbox("연도 선택", list(range(2015, 2025)))

    df_year = df[df["year"] == selected_year].copy()

    fuel_order = ["휘발유", "경유", "LPG", "전기", "CNG", "하이브리드", "수소", "기타"]
    available_fuels = [f for f in fuel_order if f in df_year["fuel_name"].unique()]
    df_year["fuel_name"] = pd.Categorical(df_year["fuel_name"], categories=available_fuels, ordered=True)

    grouped = df_year.groupby("fuel_name")["amount"].sum().reset_index()
    grouped = grouped.sort_values("amount", ascending=False)

    fuel_colors = {
        "휘발유": "#FF0000", "경유": "#808080", "LPG": "#FFA500",
        "전기": "#0000FF", "CNG": "#00BFFF", "하이브리드": "#008000",
        "수소": "#800080", "기타": "#A52A2A"
    }

    fig = px.bar(
        grouped,
        x="fuel_name",
        y="amount",
        text="amount",
        color="fuel_name",
        color_discrete_map=fuel_colors,
        labels={"fuel_name": "연료 종류", "amount": "차량 수"},
        title=f"{selected_year}년 연료별 차량 수 순위"
    )

    fig.update_traces(texttemplate='%{text:,}', textposition='outside')

    # Y축 최대값 기준 1.5배
    y_max = grouped["amount"].max() * 1.5

    fig.update_layout(
        yaxis=dict(tickformat=",d", range=[0, y_max]),
        xaxis=dict(title=dict(text="연료 종류", font=dict(size=16))),
        yaxis_title=dict(text="차량 수", font=dict(size=16)),
        font=dict(family="Malgun Gothic"),
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)