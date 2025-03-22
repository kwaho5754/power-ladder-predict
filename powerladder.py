from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# ChromeDriver 경로 설정
chrome_driver_path = "./chromedriver.exe"  # chromedriver.exe 경로

# Selenium WebDriver 설정
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창을 띄우지 않고 실행
driver = webdriver.Chrome(service=service, options=options)

# 파워사다리 사이트 접속
url = "https://ntry.com/_m/scores/power_ladder/main.php"
driver.get(url)

# 페이지가 로드될 때까지 대기
time.sleep(3)

# 데이터 크롤링 (사이트에서 표 데이터 가져오기)
data = []  # 데이터를 저장할 리스트

rows = driver.find_elements(By.CSS_SELECTOR, "#round-history tr")  # 테이블 행 선택

for row in rows[1:]:  # 첫 번째 행은 헤더이므로 제외
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 4:  # 데이터가 4개 이상 있는지 확인
        회차 = cols[0].text.strip()
        날짜 = cols[1].text.strip()
        결과 = cols[2].text.strip()
        줄수 = cols[3].text.strip()

        data.append([회차, 날짜, 결과, 줄수])  # 리스트에 추가

# WebDriver 종료
driver.quit()

# 가져온 데이터 확인 (디버깅용)
print("📌 가져온 데이터 예시:")
for d in data[:5]:  # 상위 5개만 출력
    print(d)

# CSV 파일로 저장
df = pd.DataFrame(data, columns=["회차", "날짜", "결과", "줄수"])
df.to_csv("powerladder_data.csv", index=False, encoding="utf-8-sig")

print("✅ CSV 파일이 성공적으로 저장되었습니다!")
