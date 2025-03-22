from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

# 크롬 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # 최신 Headless 모드 사용
chrome_options.add_argument("--disable-gpu")  # GPU 가속 비활성화
chrome_options.add_argument("--disable-software-rasterizer")  # 소프트웨어 렌더링도 비활성화
chrome_options.add_argument("--disable-dev-shm-usage")  # 공유 메모리 비활성화
chrome_options.add_argument("--no-sandbox")  # 샌드박스 모드 비활성화
chrome_options.add_argument("--log-level=3")  # 불필요한 오류 메시지 최소화
chrome_options.add_argument("--disable-logging")  # 크롬 로그 기능 비활성화
chrome_options.add_argument("--remote-debugging-port=9222")  # 디버깅 포트 설정
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # 봇 탐지 방지

# 크롬 드라이버 실행
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 크롤링할 사이트 URL
url = "https://ntry.com/scores/power_ladder/live.php"
driver.get(url)

# 페이지 로딩 대기
time.sleep(5)

# 타이머 값 가져오기
try:
    countdown_element = driver.find_element(By.ID, "countdown_clock")
    countdown_text = countdown_element.text
    print("현재 타이머 값:", countdown_text)

    # 정규 표현식을 이용해 숫자 변환
    match = re.search(r"(\d+)분\s*(\d+)초", countdown_text)
    if match:
        minutes = int(match.group(1))
        seconds = int(match.group(2))
        total_seconds = minutes * 60 + seconds
        print(f"총 남은 시간(초): {total_seconds}초")

        # 특정 조건 충족 시 추가 작업 실행
        if total_seconds <= 30:
            print("🚨 게임 시작 임박! 크롤링 시작 준비")
    
    else:
        print("❌ 시간 값을 찾을 수 없습니다.")

except:
    print("❌ 데이터를 찾을 수 없습니다. HTML 구조를 다시 확인하세요.")

# 브라우저 종료
driver.quit()

