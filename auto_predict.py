import pandas as pd
import json
from collections import Counter

def run_prediction():
    # CSV 파일 불러오기
    df = pd.read_csv("powerladder_data.csv")

    # 필요한 열만 사용
    required_columns = ['좌삼짝', '우삼홀', '좌사홀', '우사짝']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("CSV 파일에 필요한 열이 없습니다.")

    # 최근 회차 가져오기
    if '회차' in df.columns:
        last_round = df['회차'].iloc[-1]
    else:
        last_round = '알 수 없음'

    # 최근 200회 데이터 사용
    recent_df = df[required_columns].tail(200)

    # 조합 문자열 생성 (예: 좌삼짝-우삼홀-좌사홀-우사짝)
    recent_df["조합"] = recent_df[required_columns].astype(str).agg("-".join, axis=1)

    # 조합별 빈도수 계산
    counter = Counter(recent_df["조합"])
    top_3 = counter.most_common(3)

    # 결과 정리
    result_dict = {
        "현재 회차": last_round
    }
    for i, (combo, count) in enumerate(top_3):
        rank = f"{i+1}위"
        combo_list = combo.split("-")
        result_dict[rank] = combo_list[0] if len(combo_list) > 0 else "없음"

    # 결과 JSON 저장
    with open("latest_result.json", "w", encoding="utf-8") as f:
        json.dump({"result": result_dict}, f, ensure_ascii=False)

    return result_dict
