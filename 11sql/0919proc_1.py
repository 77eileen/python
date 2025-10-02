# 데이터베이스 연결
    # 환경변수 로드
    # os를 이용해서 환경변수의 값을 읽어서 connection 객체를 생성
    # 커넥션 객체의 cursor 객체를 생성
    # 커서 객체의 callproc('AddCodeWithTransaction', [ , , , ])
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
    database='sqldb')

print('접속성공')


# 프로시져 호출
# 커넥션 객체의 cursor 객체를 생성
# 커서 객체의 callproc('AddCodeWithTransaction', [ , , , ])
with conn as conn:
    with conn.cursor() as cursor:
        cursor.callproc('AddCodeWithTransaction', ['PROD', 'P1002', '크루아상', 0, 'Y'])
        for row in cursor.fetchall():
            print(row)
    conn.commit()

# 에러발생 ('error transaction rollback',)
# 성공 ('code added success',)