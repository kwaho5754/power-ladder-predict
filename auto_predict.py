import requests
from bs4 import BeautifulSoup
from collections import Counter
import pandas as pd

def get_current_round():
    try:
        url = "https://ntry.com/scores/power_ladder/live.php"
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        # 회차 정보를 추출하는 부분
        round_tag = soup.select_one(".wrap .tit")
        if round_tag:
            round_text = round_tag.text.strip()
            return round_text  # 예: "2025-03-28-274"
        return "회차 정보 없음"
    except Exception as e:
        return f"회차 정보 오류: {e}"

def load_data():
    df = pd.read_csv("powerladder_data.csv")
    df["조합"] = df["좌삼짝"] + "-" + df["우삼홀"] + "-" + df["좌사홀"] + "-" + df["우사짝"]
    return df

def predict(df):
    counter = Counter(df["조합"])
    most_common = counter.most_common(3)
    top_predictions = [x[0].split("-")[0] for x in most_common]  # 1위~3위 하나씩만
    return top_predictions

if __name__ == "__main__":
    current_round = get_current_round()
    df = load_data()
    predictions = predict(df)

    print("✅ 예측 실행 완료")
    print(f"🕓 현재 회차: {current_round}")
    print("🎯 예측 결과:")
    print(f"1위: {predictions[0]}")
    print(f"2위: {predictions[1]}")
    print(f"3위: {predictions[2]}")
