import pandas as pd
import json
from collections import Counter

def run_prediction():
    df = pd.read_csv("powerladder_data.csv")

    required_columns = ['좌삼짝', '우삼홀', '좌사홀', '우사짝']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("CSV 파일에 필요한 열이 없습니다.")

    # 현재 회차 추정
    last_round = df['회차'].iloc[-1] if '회차' in df.columns else '알 수 없음'

    recent_df = df[required_columns].tail(200)
    recent_df["조합"] = recent_df[required_columns].astype(str).agg("-".join, axis=1)

    counter = Counter(recent_df["조합"])
    top_combos = counter.most_common()

    index_to_name = {0: '좌삼짝', 1: '우삼홀', 2: '좌사홀', 3: '우사짝'}
    used_predictions = set()
    result_dict = {
        "현재 회차": last_round
    }

    rank_num = 1
    for combo, count in top_combos:
        if rank_num > 3:
            break
        combo_list = combo.split("-")
        for idx, val in enumerate(combo_list):
            if val == '1':
                name = index_to_name.get(idx, '알 수 없음')
                if name not in used_predictions:
                    result_dict[f"{rank_num}위"] = name
                    used_predictions.add(name)
                    rank_num += 1
                break

    # 결과가 부족하면 "없음"으로 채우기
    for i in range(rank_num, 4):
        result_dict[f"{i}위"] = "없음"

    with open("latest_result.json", "w", encoding="utf-8") as f:
        json.dump({"result": result_dict}, f, ensure_ascii=False)

    return result_dict
