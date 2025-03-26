import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re

# 1. 크롬 드라이버 설정
options = Options()
options.add_argument('--headless')  # 창 없이 실행
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(options=options)

# 2. 사이트 접속
url = 'https://ntry.com/scores/power_ladder/live.php'
browser.get(url)
time.sleep(5)  # 페이지 로딩 대기

# 3. 페이지 소스 파싱
soup = BeautifulSoup(browser.page_source, 'html.parser')

# 4. 회차 추출
round_tag = soup.select_one('h2.section_tit')
round_text = round_tag.text.strip() if round_tag else '회차 정보 없음'

# 5. 결과 추출
balls = soup.select('div.balls_wrap div.result_ball')
results = [ball.text.strip() for ball in balls if ball.text.strip()]
result_str = ' / '.join(results) if results else '결과 없음'

# 6. 좌삼짝/우삼홀/좌사홀/우사짝 추출용 패턴 분석 (예시)
pattern_block = soup.select_one('div.pie_graph ul.info')
pattern_results = []
if pattern_block:
    items = pattern_block.select('li')
    for item in items:
        text = item.text.strip()
        pattern_results.append(text)

# 7. 예측 모델 흉내 (임시) - 실제 모델 연결 가능
prediction = '1위: 좌삼짝, 2위: 우삼홀, 3위: 좌사홀'

# 8. 출력
print("[회차]", round_text)
print("[결과]", result_str)
print("[패턴 통계]")
for stat in pattern_results:
    print(" ", stat)
print("[예측 결과]", prediction)

# 9. 종료
browser.quit()

# 10. 반복 실행 원할 시 아래 주석 해제 → 일정 간격 반복 실행 가능
# while True:
#     main()
#     time.sleep(60)  # 1분마다 반복
