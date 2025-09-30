# x = '2.5'
# print(float(x))
# print(float('2.5'))
# print(float(2.5))

# a="hello world"
# a.split



import mysql.connector

try:
    # MySQL 연결
    conn = mysql.connector.connect(
        host="localhost",   # 또는 127.0.0.1
        user="root",        # 본인 MySQL 아이디
        password="root1234", # 본인 MySQL 비밀번호
        port=3306
    )
    
    print("✅ MySQL 서버 연결 성공!")

    conn.close()
except mysql.connector.Error as err:
    print("❌ MySQL 연결 실패:", err)
