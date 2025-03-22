from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Chrome WebDriver 경로 (chromedriver.exe 위치 지정)
chrome_driver_path = "C:/Users/kwanh/chromedriver.exe"

service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # 브라우저 창 최대화
options.add_experimental_option("detach", True)  # 브라우저가 자동 종료되지 않도록 설정

# 크롬 브라우저 실행
driver = webdriver.Chrome(service=service, options=options)

# 📌 파워사다리 사이트 열기
url = "https://ntry.com/scores/power_ladder/main.php"
driver.get(url)

# 수집된 데이터 저장 리스트
data_list = []

def collect_data():
    """ 웹사이트에서 데이터를 가져오는 함수 """
    try:
        # 📌 실제 데이터를 포함하는 요소를 찾기 (개발자 도구에서 클래스명 확인 후 수정)
        elements = driver.find_elements(By.CLASS_NAME, "score-data")  # CLASS_NAME 수정 필요
        
        # 가져온 데이터 리스트 저장
        current_data = [elem.text for elem in elements]

        # 중복 데이터 방지
        if current_data and current_data not in data_list:
            data_list.append(current_data)
            print("✅ 수집된 데이터:", current_data)

    except Exception as e:
        print("❌ 데이터 수집 오류:", e)

# **5초마다 자동으로 데이터 수집**
while True:
    collect_data()
    time.sleep(5)
