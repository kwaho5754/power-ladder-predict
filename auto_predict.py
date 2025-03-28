import pandas as pd
import json
from collections import Counter
import requests
from bs4 import BeautifulSoup

def get_current_round():
    try:
        url = "https://ntry.com/scores/power_ladder/live.php"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        round_element = soup.select_one(".ladder_num span")
        if round_element:
            return round_element.text.strip()
    except Exception as e:
        print("⚠️ 회차 불러오기 실패:", e)
    return "알 수 없음"

def run_prediction():
    # CSV 파일 불러오기
    df = pd.read_csv("powerladder_data.csv")

    # 필요한 열
    required_columns = ['좌삼짝', '우삼홀', '좌사홀', '우사짝']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("CSV 파일에 필요한 열이 없습니다.")

    # 최근 200회 기준
    recent_df = df[required_columns].tail(200)

    # 조합 문자열 생성 (문자열 변환 후 결합)
    recent_df["조합"] = recent_df[required_columns].astype(str).agg("-".join, axis=1)

    # 빈도수 계산
    counter = Counter(recent_df["조합"])

    # 가장 많이 나온 상위 3개
    top_3 = counter.most_common(3)

    # 조합에서 첫 번째 항목만 추출
    result_dict = {}
    for i, (combo, _) in enumerate(top_3):
        rank = f"{i+1}위"
        parts = combo.split("-")
        result_dict[rank] = parts[0] if len(parts) > 0 else "없음"

    # 회차 정보 추가
    result_dict["회차"] = get_current_round()

    # JSON 저장
    with open("latest_result.json", "w", encoding="utf-8") as f:
        json.dump({"result": result_dict}, f, ensure_ascii=False)

    return result_dict
