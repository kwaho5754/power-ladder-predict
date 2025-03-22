from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# 1. 웹드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창을 띄우지 않음 (필요하면 주석 처리)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 2. 메인 페이지 접속
main_url = "https://ntry.com/scores/power_ladder/main.php"
driver.get(main_url)
time.sleep(3)  # 페이지 로딩 대기

# 3. iframe으로 전환
iframe_url = "https://ntry.com/scores/power_ladder/live.php"
driver.get(iframe_url)
time.sleep(3)

# 4. HTML 가져오기
html = driver.page_source
driver.quit()  # 브라우저 닫기

# 5. BeautifulSoup으로 데이터 확인
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 6. HTML 일부 출력 (데이터 구조 확인용)
print("iframe 내부 HTML 미리보기:")
print(soup.prettify()[:1000])  # 1000자 출력
