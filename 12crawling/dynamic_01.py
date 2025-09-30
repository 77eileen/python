
# pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  #크롬 드라이버 실행을 도와줌
from webdriver_manager.chrome import ChromeDriverManager #크롬드라이버 자동 설치/업데이트 도우미
from selenium.webdriver.common.by import By  #페이지요소 찾을 떄 기준 지정 도구
from selenium.webdriver.common.keys import Keys  # enter키 등을 입력하기위해서
import time
#웹 드라이버를 자동으로 설치하고 최신버전을 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com/')
time.sleep(3)
print('브라우져가 성공적으로 열렸습니다.')
# 검색창 요소 찾기 (id 가 'ipt_keyword_recruit' 인 input 태그를 찾음)
search_input = driver.find_element(By.CLASS_NAME,'gLFyf')  #F12에서 select element..클릭해서 검색창 하늘색을 클릭하면 class=gLFyf 가 확인됨 
#검색창에 파이썬  입력
search_input.send_keys('파이썬')
time.sleep(3)
# Enter키 누르기
search_input.send_keys(Keys.ENTER)
time.sleep(5)
driver.quit()