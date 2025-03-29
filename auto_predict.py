import pandas as pd
import json
from collections import Counter

def run_prediction():
    df = pd.read_csv("powerladder_data.csv")

    required_columns = ['좌삼짝', '우삼홀', '좌사홀', '우사짝']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("CSV 파일에 필요한 열이 없습니다.")

    # 최근 200회 데이터 사용
    recent_df = df[required_columns].tail(200)

    # 조합 문자열 생성 (조합 이름을 그대로 사용)
    def get_combination(row):
        for col in required_columns:
            if row[col] == 1:
                return col
        return "없음"

    # 조합열 생성
    recent_df["조합"] = recent_df.apply(get_combination, axis=1)

    # 조합별 빈도 계산
    counter = Counter(recent_df["조합"])
    top_3 = counter.most_common(3)

    # 결과 딕셔너리 생성
    result_dict = {"회차": "알 수 없음"}
    for i, (name, count) in enumerate(top_3):
        순위 = f"{i+1}위"
        result_dict[순위] = name

    # JSON 저장
    with open("latest_result.json", "w", encoding="utf-8") as f:
        json.dump({"result": result_dict}, f, ensure_ascii=False)

    return result_dict

# 로컬 테스트용
if __name__ == "__main__":
    result = run_prediction()
    print(result)
