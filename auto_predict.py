import pandas as pd
import json
from collections import Counter
from scrape_round import get_current_round

def run_prediction():
    # CSV 파일 불러오기
    df = pd.read_csv("powerladder_data.csv")

    # 필요한 열만 사용
    required_columns = ['좌삼짝', '우삼홀', '좌사홀', '우사짝']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("CSV 파일에 필요한 열이 없습니다.")

    # 최근 200회 데이터 사용
    recent_df = df[required_columns].tail(200)

    # 조합 문자열 생성
    recent_df["조합"] = recent_df[required_columns].astype(str).agg("-".join, axis=1)

    # 조합별 빈도수 계산
    counter = Counter(recent_df["조합"])

    # 가장 많이 등장한 상위 3개 조합 추출
    top_3 = counter.most_common(3)

    # 결과 정리
    result_dict = {}
    pattern_map = {0: "좌삼짝", 1: "우삼홀", 2: "좌사홀", 3: "우사짝"}
    for i, (combo, count) in enumerate(top_3):
        순위 = f"{i+1}위"
        조합_리스트 = combo.split("-")
        if len(조합_리스트) != 4:
            result_dict[순위] = "없음"
        else:
            top_idx = [idx for idx, val in enumerate(조합_리스트) if val == "1"]
            result_dict[순위] = pattern_map[top_idx[0]] if top_idx else "없음"

    # 현재 회차 정보 포함
    result_dict["회차"] = get_current_round()

    # 결과 저장
    with open("latest_result.json", "w", encoding="utf-8") as f:
        json.dump({"result": result_dict}, f, ensure_ascii=False)

    return result_dict

if __name__ == "__main__":
    run_prediction()
