from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. 웹드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창을 띄우지 않음
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 2. iframe URL 접속
iframe_url = "https://ntry.com/scores/power_ladder/live.php"
driver.get(iframe_url)

# 3. 특정 요소가 나타날 때까지 기다리기 (예: 결과 테이블)
try:
    # 예시: 10초 동안 특정 요소가 나타날 때까지 기다림
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))  # 테이블이 로드될 때까지 대기
    )
    print("✅ 데이터가 로드되었습니다!")
except:
    print("⚠️ 데이터를 찾을 수 없습니다!")

# 4. HTML 가져오기
html = driver.page_source
driver.quit()  # 브라우저 닫기

# 5. BeautifulSoup으로 데이터 확인
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 6. HTML 일부 출력 (데이터 구조 확인용)
print("iframe 내부 HTML 미리보기:")
print(soup.prettify()[:1000])  # 1000자 출력
