from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# 1. 웹드라이버 설정 및 브라우저 열기
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창을 띄우지 않음 (원하면 주석 처리)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 2. 파워사다리 사이트 접속
url = "https://ntry.com/scores/power_ladder/main.php"
driver.get(url)

# 페이지가 완전히 로드될 때까지 대기
time.sleep(3)

# 3. HTML 가져오기
html = driver.page_source
driver.quit()  # 브라우저 닫기

# 4. BeautifulSoup으로 데이터 추출
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 5. 원하는 데이터 찾기 (일단 div 태그 전체 출력)
print("페이지 내용 미리보기:")
print(soup.prettify()[:1000])  # HTML 앞부분 1000자 출력
