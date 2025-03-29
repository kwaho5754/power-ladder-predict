import pandas as pd
import json
from collections import Counter

def run_prediction():
    # CSV 파일 불러오기
    df = pd.read_csv("powerladder_data.csv")

    # 필요한 열 확인
    required_columns = ['좌삼짝', '우삼홀', '좌사홀', '우사짝']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("CSV 파일에 필요한 열이 없습니다.")

    # 최근 200회 데이터 사용
    recent_df = df[required_columns].tail(200)

    # 조합 문자열 생성
    recent_df["조합"] = recent_df[required_columns].astype(str).agg("-".join, axis=1)

    # 빈도 계산
    counter = Counter(recent_df["조합"])
    top_3 = counter.most_common(3)

    # 예측 결과 정리
    result_dict = {}
    for i, (combo, count) in enumerate(top_3):
        순위 = f"{i+1}위"
        조합리스트 = combo.split("-")
        result_dict[순위] = 조합리스트[0] if len(조합리스트) > 0 else "없음"

    # 회차 정보 저장 (실시간 못 가져오면 기본값)
    result_dict["회차"] = "알 수 없음"

    # JSON 저장
    with open("latest_result.json", "w", encoding="utf-8") as f:
        json.dump({"result": result_dict}, f, ensure_ascii=False)

    return result_dict

# 로컬 테스트용
if __name__ == "__main__":
    result = run_prediction()
    print(result)
