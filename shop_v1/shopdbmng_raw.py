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

#2. 각 테이블별 CRUD
    #C - insert
    #R - select
    #U - update
    #D - delete
# 고객 - customer   
    #SQL에서 insert 되는지 먼저 확인해보고 파이썬으로 가져오기

#CRUD C - insert
def create_customer(name):
    sql = 'insert into customer values (null, %s)'  
    with conn.cursor() as cur:  #데이터베이스에 접속을 실행할 수 있는 명령
        cur.execute(sql, name)   #여러개면 튜플로 묶어서 실행???
        conn.commit()    #commit 
    print(f'고객추가 완료. 고객명: {name}')
#테스트
# create_customer('지은탁')


#CRUD R - select
def readAll_customers(isDict = False):
    sql = 'select * from customer'

    if isDict:        
        #방법1
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(sql) 
            for c in cur.fetchall():
                print (f'{c['customer_id']} {c['name']}')

        
    else:
        #방법2
        with conn.cursor() as cur:
            cur.execute(sql)
            for c in cur.fetchall():
                print(f'{c[0]} {c[1]}')
    print ('조회완료')
    # read 라서 commit 필요없음

#상기 read 테스트
# readAll_customers(isDict = False)


#CRUD U - update
def update_customer (customer_id, name):
    sql= '''
        update customer
              set name = %s
        where customer_id = %s
        '''
    # cur = conn.cursor()
    # cur.execute(sql, (customer_id, name))
    # conn.commit()
    with conn.cursor() as cur:          #with ~와 함께하다... close를 안해도 블록만 벗어나면 ..??
          cur.execute(sql, (name,customer_id))
    conn.commit()
    print(f'업데이트 되었습니다. 고객아이디: {customer_id}/ 고객명:{name}')
#테스트
# update_customer('안유진', 7)

#CRUD D - delete
def delete_customer(customer_id):
    sql = 'DELETE FROM customer WHERE customer_id = %s'
    with conn.cursor() as cur:
        cur.execute(sql, customer_id)
    conn.commit()
    print(f'삭제 되었습니다. 삭제된 고객아이디 :{customer_id}')


#전체 테스트
create_customer('손예진')
readAll_customers()
update_customer(9,'송혜교')
delete_customer(4)


#3. 메소드
    # 회원가입
    # 상품정보 출력
    # 상품구입
    # 상품정보 입력
    # 대쉬보드: 고객별 상품별 구매회수, 평균구매액
#4. 기능구현과 테스트가 되면.. streamlit 으로 UI 구성 - 템플릿 화면을 보고 유사한 형태로 구현

conn.close() #접속해제