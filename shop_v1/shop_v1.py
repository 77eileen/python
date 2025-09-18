#pip install pymysql  #mysql을 접속할 수 있는 라이브러리
#pip install dotenv  #환경변수 .env를 로드할 수 있는 라이브러리
#가상환경설정
#파일 및 실행 - streamlit_prj 선택 - 터미널창 오른쪽+에 command prompt 선택

import pymysql 
from dotenv import load_dotenv
import os

#.env로드
load_dotenv()

#1. DB연결
conn=pymysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME'))

print('접속성공')
conn.close() #접속해제
#2. 각 테이블별 CRUD
    #C - insert
    #R - select
    #U - update
    #D - delete
#3. 메소드
    # 회원가입
    # 상품정보 출력
    # 상품구입
    # 상품정보 입력
    # 대쉬보드: 고객별 상품별 구매회수, 평균구매액
#4. 기능구현과 테스트가 되면.. streamlit 으로 UI 구성 - 템플릿 화면을 보고 유사한 형태로 구현

