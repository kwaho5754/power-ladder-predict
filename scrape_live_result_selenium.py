from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# 1. 크롬 드라이버 설정
options = Options()
options.add_argument('--headless')  # 창을 띄우지 않음
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 2. 드라이버 실행 및 URL 접속
browser = webdriver.Chrome(options=options)
url = 'https://ntry.com/scores/power_ladder/live.php'
browser.get(url)

# 3. 페이지 로딩 대기
time.sleep(5)

# 4. 페이지 소스 가져오기
soup = BeautifulSoup(browser.page_source, 'html.parser')

# 5. 회차 정보 추출
round_tag = soup.select_one('div#score_board span.curr_round strong')
round_text = round_tag.text.strip() if round_tag else '회차 정보 없음'

# 6. 결과 정보 추출
balls = soup.select('div.balls_wrap div.result_ball')
results = [ball.text.strip() for ball in balls if ball.text.strip()]

# 7. 출력
print(f"[회차] {round_text}")
print(f"[결과] {' / '.join(results) if results else '결과 없음'}")

# 8. 종료
browser.quit()
