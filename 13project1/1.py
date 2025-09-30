import pandas as pd

# Excel 파일 읽기
df = pd.read_excel("파일경로/파일명.xlsx", sheet_name="Sheet1")  # sheet_name 생략하면 첫 번째 시트 읽음

# 데이터 확인
print(df.head())
