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

    # 최근 200회 데이터 사용
    recent_df = df[required_columns].tail(200)

    # 조합 문자열 생성 (예: 좌삼짝-우삼홀-좌사홀-우사짝)
    recent_df["조합"] = recent_df[required_columns].agg("-".join, axis=1)

    # 조합별 빈도수 계산
    counter = Counter(recent_df["조합"])

    # 가장 많이 등장한 상위 3개 조합 추출
    top_3 = counter.most_common(3)

    # 결과 정리: 각 조합에서 첫 번째 항목만 추출 (1위는 좌삼짝 같은 형식)
    result_dict = {}
    for i, (combo, count) in enumerate(top_3):
        순위 = f"{i+1}위"
        조합_리스트 = combo.split("-")
        result_dict[순위] = 조합_리스트[0]

    # 결과를 JSON 파일로 저장
    with open("latest_result.json", "w", encoding="utf-8") as f:
        json.dump({"result": result_dict}, f, ensure_ascii=False)

    # 콘솔 출력
    print("✅ 예측 결과:")
    for rank, value in result_dict.items():
        print(f"{rank}: {value}")

    return result_dict

# 직접 실행 시
if __name__ == "__main__":
    run_prediction()
