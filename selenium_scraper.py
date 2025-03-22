# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Chrome 브라우저 설정
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 화면 없이 실행하는 옵션 (필수 아님)
options.add_argument("--disable-gpu")  # GPU 가속 비활성화 (안정성 증가)

# Chrome 드라이버 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 크롤링할 URL 지정
url = "https://ntry.com/stats/power_ladder/pattern.php"  # 패턴 분석 페이지
driver.get(url)

# 페이지 로딩 대기
time.sleep(3)  # 3초 대기 (필요시 조정)

# HTML 데이터 가져오기
html = driver.page_source

# BeautifulSoup을 사용하여 데이터 파싱
soup = BeautifulSoup(html, "html.parser")

# 테이블 데이터 가져오기 (테이블 태그 찾기)
table = soup.find("table")  # 가장 첫 번째 테이블 찾기
rows = table.find_all("tr")  # 테이블의 모든 행 찾기

# 데이터 추출 및 가독성 향상
cleaned_data = []
for row in rows:
    columns = row.find_all("td")  # 각 행의 모든 데이터 셀 찾기
    data = [col.text.strip().replace("\n", " ") for col in columns]  # 공백 및 개행문자 제거
    if data:  # 빈 리스트 방지
        cleaned_data.append(data)

# 정리된 데이터 출력
for row in cleaned_data:
    print(" | ".join(row))  # 데이터 사이에 ' | ' 구분자 추가하여 출력

# Selenium 종료
driver.quit()
