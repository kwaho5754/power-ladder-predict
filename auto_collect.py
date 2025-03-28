import time
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os

# CSV 파일 이름
CSV_FILE = 'powerladder_data.csv'

# 셀레니움 옵션
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# 크롬 드라이버 경로 설정 (이미 render에서는 자동 설정됨)
driver = webdriver.Chrome(options=options)

def scrape_latest_result():
    url = 'https://www.entropygame.co.kr/powerladder'
    driver.get(url)
    time.sleep(2)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    try:
        result_area = soup.select_one('.result_area')
        round_number = result_area.select_one('.date').text.strip()
        result_texts = result_area.select('.ball span')

        # 좌삼짝, 우삼홀, 좌사홀, 우사짝 순서로 텍스트 추출
        result = {
            'round': round_number,
            '좌삼짝': result_texts[0].text.strip(),
            '우삼홀': result_texts[1].text.strip(),
            '좌사홀': result_texts[2].text.strip(),
            '우사짝': result_texts[3].text.strip(),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        return result
    except Exception as e:
        print('오류:', e)
        return None

def save_to_csv(result):
    if result is None:
        return
    df = pd.DataFrame([result])
    if not os.path.exists(CSV_FILE):
        df.to_csv(CSV_FILE, index=False, encoding='utf-8-sig')
    else:
        df.to_csv(CSV_FILE, mode='a', header=False, index=False, encoding='utf-8-sig')
    print("저장 완료:", result['round'])

if __name__ == '__main__':
    result = scrape_latest_result()
    save_to_csv(result)
    driver.quit()
