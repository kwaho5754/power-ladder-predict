import schedule
import subprocess
import time

# 데이터 수집 자동 실행
def run_scraper():
    print("🌐 웹 스크래핑 실행 중...")
    subprocess.run(["python", "scraper.py"])

# 예측 실행
def run_predict():
    print("🔮 예측 실행 중...")
    subprocess.run(["python", "predict.py"])

# 일정 시간마다 실행 (5분 간격)
schedule.every(5).minutes.do(run_scraper)
schedule.every(5).minutes.do(run_predict)

# 무한 루프 실행
while True:
    schedule.run_pending()
    time.sleep(1)
