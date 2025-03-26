from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# 1. 크롬 드라이버 설정
options = Options()
options.add_argument('--headless')  # 창을 띄우지 않음
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(options=options)
url = 'https://ntry.com/stats/power_ladder/pattern.php'
browser.get(url)

# 2. 페이지 로딩 대기
time.sleep(3)

# 3. 페이지 소스 파싱
soup = BeautifulSoup(browser.page_source, 'html.parser')

# 4. 패턴 리스트 추출
pattern_list = soup.select('ul#latest_pattern_list li')

# 5. 결과 출력
print("[✓] 패턴 분석 결과 미리보기:")
for li in pattern_list[:10]:  # 최근 10개만 출력
    count = li.select_one('.count').text.strip()
    result = li.select_one('.ic_result').text.strip()
    round_num = li.select_one('.round').text.strip()
    print(f"{count:>2}회 | {round_num} | {result}")

# 6. 종료
browser.quit()
