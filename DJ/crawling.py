# =========================================
# 1️⃣ 필요한 모듈 불러오기
# =========================================
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector
import time
import pandas as pd
import streamlit as st

# =========================================
# 2️⃣ Selenium 크롤링 설정
# =========================================
# chromedriver를 자동 다운로드 후 연결
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 현대자동차 FAQ 페이지 열기
driver.get('https://www.hyundai.com/kr/ko/faq.html')

# 최대 15초 동안 FAQ 항목이 나타날 때까지 기다리기
wait = WebDriverWait(driver, 15)

# FAQ 데이터를 저장할 리스트
faq_data = []

# =========================================
# 3️⃣ 1~3페이지 반복 크롤링
# =========================================
for page_num in range(1, 3):  # 1페이지부터 3페이지까지만 반복
    print(f"=== {page_num} 페이지 크롤링 시작 ===")
    
    # 현재 페이지 FAQ 리스트 가져오기
    faq_items = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div.ui_accordion.acc_01 dl")
    ))

    for i, faq in enumerate(faq_items, start=1):
        try:
            question_button = faq.find_element(By.CSS_SELECTOR, "dt button")
            # JS로 클릭 (다른 요소에 가려져도 클릭 가능)
            driver.execute_script("arguments[0].click();", question_button)
            time.sleep(0.3)  # 답변 로딩 잠시 대기
            answer_text = faq.find_element(By.CSS_SELECTOR, "dd").text
            faq_data.append((question_button.text, answer_text))
            
            # 중간 확인용 출력
            print(f"{i}번 질문: {question_button.text}")
            print(f"답변: {answer_text[:50]}...")
        except Exception as e:
            print(f"{i}번 FAQ 처리 중 오류:", e)
    
    # 다음 페이지 버튼 클릭 (마지막 페이지는 클릭 안 함)
    if page_num < 5:  # 5페이지까지만 크롤링
        try:
            next_btn = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#contents div.ui_paging.plugin-paging-apply nav button.navi.next")
            ))
            driver.execute_script("arguments[0].click();", next_btn)
            time.sleep(1)  # 페이지 로딩 대기
        except Exception as e:
            print(f"{page_num} 페이지 다음 버튼 클릭 오류:", e)

driver.quit()
print("총 FAQ 개수:", len(faq_data))

# =========================================
# 4️⃣ MySQL에 저장
# =========================================
try:
    # DB 연결 (직접 문자열로 지정)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root1234"  # 본인 MySQL 비밀번호
    )
    cur = conn.cursor()
except Exception as e:
    print("DB 연결 실패:", e)
    raise SystemExit

# 2. 데이터베이스 생성
cur.execute("CREATE DATABASE IF NOT EXISTS 0dj_test")
print("데이터베이스 '0dj_test' 생성 완료 또는 이미 존재함")
cur.execute("USE 0dj_test")

# 3. 테이블 생성
cur.execute("""
CREATE TABLE IF NOT EXISTS faq (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT,
    answer TEXT
)
""")
print("테이블 'faq' 생성 완료 또는 이미 존재함")

# 4. FAQ 데이터를 DB에 저장
for q, a in faq_data:
    cur.execute("INSERT INTO faq (question, answer) VALUES (%s, %s)", (q, a))

# 5. 변경 사항 커밋 및 연결 종료
conn.commit()
cur.close()
conn.close()
print("MySQL 저장 완료!")

# =========================================
# 5️⃣ Streamlit 화면에 출력
# =========================================
# MySQL에서 데이터 읽어오기
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root1234",
        database="0dj_test"
    )
    df = pd.read_sql("SELECT * FROM faq", conn)
    conn.close()
    
    # Streamlit 화면 구성
    st.title("현대자동차 FAQ")   # 제목 표시
    st.dataframe(df)            # 표 형태로 FAQ 보여주기
except Exception as e:
    st.write("Streamlit DB 로딩 오류:", e)
