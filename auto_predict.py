import pandas as pd
import json
from collections import Counter

def run_prediction():
    # CSV 불러오기
    df = pd.read_csv("powerladder_data.csv")

    # 사용할 열
    required_columns = ['좌삼짝', '우삼홀', '좌사홀', '우사짝']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("CSV 파일에 필요한 열이 없습니다.")

    # 현재 회차 추정
    last_round = df['회차'].iloc[-1] if '회차' in df.columns else '알 수 없음'

    # 최근 200회만 사용
    recent_df = df[required_columns].tail(200)

    # 조합 문자열 생성
    recent_df["조합"] = recent_df[required_columns].astype(str).agg("-".join, axis=1)

    # 조합 빈도수 계산
    counter = Counter(recent_df["조합"])
    top_3 = counter.most_common(3)

    # 숫자 인덱스를 열 이름으로 변환
    index_to_name = {0: '좌삼짝', 1: '우삼홀', 2: '좌사홀', 3: '우사짝'}

    result_dict = {
        "현재 회차": last_round
    }

    for i, (combo, count) in enumerate(top_3):
        rank = f"{i+1}위"
        combo_list = combo.split("-")
        # 가장 먼저 등장하는 값이 1인 조합 항목을 찾음
        prediction = "없음"
        for idx, val in enumerate(combo_list):
            if val == '1':
                prediction = index_to_name.get(idx, '알 수 없음')
                break
        result_dict[rank] = prediction

    # 결과 저장
    with open("latest_result.json", "w", encoding="utf-8") as f:
        json.dump({"result": result_dict}, f, ensure_ascii=False)

    return result_dict
