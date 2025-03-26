from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# 1. 브라우저 설정 및 열기
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=options)

url = 'https://ntry.com/stats/power_ladder/date.php'
browser.get(url)

# 2. JavaScript 실행 시간 대기
time.sleep(5)

# 3. 페이지 소스 파싱
soup = BeautifulSoup(browser.page_source, 'html.parser')
table = soup.find('table')

# 4. 테이블을 데이터프레임으로 변환
if table:
    df = pd.read_html(str(table))[0]
    print("[✓] 일별 분석 테이블 미리보기:")
    print(df.head())
else:
    df = None
    print("[!] 테이블을 찾을 수 없습니다.")

# 5. 브라우저 종료
browser.quit()
