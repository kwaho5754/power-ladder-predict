import time
import subprocess

# 무한 루프 시작
while True:
    print("\n[🔁 자동 예측 실행 - 현재 시각:", time.strftime("%H:%M:%S"), "]")
    
    # 실시간 데이터 분석 및 예측 스크립트 실행
    subprocess.run(["python", "scrape_live_result_selenium.py"])
    subprocess.run(["python", "scrape_analysis_pages.py"])

    # 1분 대기 후 반복
    print("[⏳ 1분 대기 후 다음 예측]")
    time.sleep(60)
