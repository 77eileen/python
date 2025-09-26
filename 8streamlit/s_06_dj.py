#copilot Agent 프롬프트:
# streamlit으로 다음과 같은 layout을 구성해줘
# 좌측에는 메뉴를 구성하고
# 메뉴를 클릭하면 우측에는 해당 메뉴의 컨텐츠가 표시되도록
# 전체 layout는 1x2 형태이고 좌측은 전체폭에서 대략 20%의 너비를 갖는 구조



import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="Streamlit 레이아웃 예제",
    layout="wide"  # 전체 화면 너비 사용
)

# 1x2 레이아웃 생성
col1, col2 = st.columns([1, 4])  # 1:4 비율 (20%:80%)

# 왼쪽 컬럼 (메뉴)
with col1:
    st.markdown("## 메뉴")
    menu_choice = st.radio(
        label="메뉴를 선택하세요",
        options=["홈", "프로필", "설정", "도움말"],
        label_visibility="collapsed"  # 라벨 숨기기
    )

# 오른쪽 컬럼 (컨텐츠)
with col2:
    if menu_choice == "홈":
        st.title("홈")
        st.write("환영합니다! 이곳은 홈 페이지입니다.")
        st.write("원하시는 메뉴를 왼쪽에서 선택해주세요.")
        
    elif menu_choice == "프로필":
        st.title("프로필")
        st.write("사용자 프로필 정보입니다.")
        # 프로필 컨텐츠 예시
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric(label="팔로워", value="1,204", delta="12")
        with col_b:
            st.metric(label="팔로잉", value="342", delta="-2")
        
    elif menu_choice == "설정":
        st.title("설정")
        st.write("앱 설정을 변경할 수 있습니다.")
        # 설정 컨텐츠 예시
        theme = st.selectbox("테마 선택", ["라이트", "다크"])
        notifications = st.checkbox("알림 받기")
        
    elif menu_choice == "도움말":
        st.title("도움말")
        st.write("도움이 필요하신가요?")
        # 도움말 컨텐츠 예시
        with st.expander("자주 묻는 질문"):
            st.write("1. 어떻게 시작하나요?")
            st.write("2. 문제가 발생했을 때는?")
            st.write("3. 연락처는 어디로?")

# 스타일 적용
st.markdown("""
    <style>
        /* 왼쪽 메뉴 스타일링 */
        div.css-1v0mbdj.e115fcil1 {
            padding: 1rem;
            background-color: #f0f2f6;
            border-radius: 10px;
        }
        
        /* 라디오 버튼 간격 조정 */
        div.st-emotion-cache-1m8qn3t.e1nzilvr5 {
            padding: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)


#streamlit run .\streamlit\s_06_dj.py

#프로젝트1
#크롤링, api를 이용해서 하나의 페이지로 만듬..?