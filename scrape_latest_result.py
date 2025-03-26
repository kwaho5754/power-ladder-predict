import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# 1. 실시간 페이지 URL
URL = "https://ntry.com/scores/power_ladder/live.php"

# 2. 요청 보내기
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# 3. 회차 결과 정보 추출
result_section = soup.select_one(".lottery_wrap")

# 회차 번호 추출
round_text = result_section.select_one(".round_txt").text.strip()
round_number = round_text.replace("회차", "").strip()

# 결과 구슬 추출 (좌삼짝, 우삼홀, 좌사홀, 우사짝 순서)
balls = result_section.select(".result_ball_line .result_ball")
ball_values = [b.text.strip() for b in balls[:4]]  # 최대 4개까지만

# 4. 시간 정보 (현재 시각 기준)
now = datetime.now()
current_time = now.strftime("%H:%M")
current_date = now.strftime("%Y-%m-%d")

# 5. API 요청 JSON 생성
payload = {
    "round": f"{current_date}-{round_number.zfill(2)}",
    "time": current_time,
    "좌삼짝": ball_values[0],
    "우삼홀": ball_values[1],
    "좌사홀": ball_values[2],
    "우사짝": ball_values[3],
}

# 6. 예측 API로 전송
API_URL = "https://power-ladder-predict.onrender.com/predict"
response = requests.post(API_URL, json=payload)

# 7. 결과 출력
if response.status_code == 200:
    print("✅ 예측 결과:", response.json()["result"])
else:
    print("❌ 예측 실패:", response.status_code, response.text)
