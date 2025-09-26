#streamlit run shop_v1\dj_ui_v2.py

import streamlit as st
import pandas as pd
import shopdbmng

# -----------------------------
# 초기 회원 데이터
# -----------------------------
if 'members' not in st.session_state:
    datas= shopdbmng.readAll_customers()
    st.session_state.members = pd.DataFrame(datas)

members = st.session_state.members

# -----------------------------
# 레이아웃 설정
# -----------------------------
left_col, right_col = st.columns([1, 3])

with left_col:
    st.header("회원 관리")
    action = st.radio("선택", ["회원 전체 조회", "회원 추가", "회원 수정", "회원 삭제"])

with right_col:
    if action == "회원 전체 조회":
        st.subheader("회원 목록")
        sort_dict = {"ID": "회원아이디", "이름": "회원이름"}
        sort_option = st.selectbox("정렬 기준", ["ID", "이름"])
        actual_column = sort_dict[sort_option]
        st.dataframe(members.sort_values(by=actual_column).reset_index(drop=True))

    elif action == "회원 추가":
        st.subheader("회원 추가")
        new_id = members['회원아이디'].max() + 1 if not members.empty else 1
        st.write(f"자동 생성 ID: {new_id}")
        new_name = st.text_input("회원 이름 입력")
        if st.button("추가"):
            if new_name.strip() == "":
                st.warning("이름을 입력해주세요.")
            else:
                shopdbmng.create_customer(new_name)
                members.loc[len(members)] = [new_id, new_name]
                st.success(f"{new_name} 회원 추가 완료")
                st.dataframe(members)

    elif action == "회원 수정":
        st.subheader("회원 수정")
        search_value = st.text_input("수정할 회원 검색 (ID 또는 이름)")
        if search_value.strip() != "":
            # 숫자면 ID 검색, 아니면 이름 검색
            if search_value.isdigit():
                filtered = members[members['회원아이디'] == int(search_value)]
            else:
                filtered = members[members['회원이름'].str.contains(search_value)]
        else:
            filtered = pd.DataFrame(columns=members.columns)
        
        if not filtered.empty:
            selected_idx = st.selectbox(
                "선택", 
                filtered.index, 
                format_func=lambda x: f"{members.loc[x, '회원아이디']} - {members.loc[x, '회원이름']}"
            )
            new_name = st.text_input("새 이름 입력", value=members.loc[selected_idx, '회원이름'])
            if st.button("수정"):
                shopdbmng.update_customer(members.loc[selected_idx, '회원아이디'], new_name)
                members.loc[selected_idx, '회원이름'] = new_name
                st.success("회원 정보 수정 완료")
                st.dataframe(members)
        else:
            st.info("검색 결과가 없습니다.")

    elif action == "회원 삭제":
        st.subheader("회원 삭제")
        search_value = st.text_input("삭제할 회원 검색 (ID 또는 이름)")
        if search_value.strip() != "":
            if search_value.isdigit():
                filtered = members[members['회원아이디'] == int(search_value)]
            else:
                filtered = members[members['회원이름'].str.contains(search_value)]
        else:
            filtered = pd.DataFrame(columns=members.columns)

        if not filtered.empty:
            selected_idx = st.selectbox(
                "선택", 
                filtered.index, 
                format_func=lambda x: f"{members.loc[x, '회원아이디']} - {members.loc[x, '회원이름']}"
            )
            if st.button("삭제"):
                customer_id = members.loc[selected_idx, '회원아이디']
                name = members.loc[selected_idx, '회원이름']
                shopdbmng.delete_customer(customer_id)
                members.drop(selected_idx, inplace=True)
                st.success(f"{name} 회원 삭제 완료")
                st.dataframe(members)
        else:
            st.info("검색 결과가 없습니다.")

