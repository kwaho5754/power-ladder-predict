from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# 1. 웹드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 브라우저 창을 띄우지 않음
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 2. 파워사다리 사이트 접속
url = "https://ntry.com/scores/power_ladder/main.php"
driver.get(url)
time.sleep(3)  # 페이지 로딩 대기

# 3. iframe이 존재하는지 확인
iframes = driver.find_elements(By.TAG_NAME, "iframe")

if iframes:
    print(f"이 페이지에는 {len(iframes)}개의 iframe이 있습니다.")
    for index, iframe in enumerate(iframes):
        print(f"{index+1}: {iframe.get_attribute('src')}")
else:
    print("iframe이 존재하지 않습니다.")

driver.quit()
