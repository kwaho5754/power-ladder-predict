import pandas as pd
import json
from collections import Counter

# 상수 정의
CSV_FILE = "powerladder_data.csv"
JSON_FILE = "latest_result.json"
REQUIRED_COLUMNS = ['좌삼짝', '우삼홀', '좌사홀', '우사짝']

def run_prediction():
    # CSV 파일 불러오기
    df = pd.read_csv(CSV_FILE)
    print("✅ CSV 파일 불러오기 완료")

    # 필요한 열 존재 확인
    if not all(col in df.columns for col in REQUIRED_COLUMNS):
        raise ValueError("CSV 파일에 필요한 열이 없습니다.")

    # 최근 200회 데이터만 사용
    recent_df = df[REQUIRED_COLUMNS].tail(200)

    # 조합 열 생성 (숫자형을 문자열로 변환하여 join)
    recent_df["조합"] = recent_df[REQUIRED_COLUMNS].astype(str).agg("-".join, axis=1)

    # 조합별 빈도수 계산
    counter = Counter(recent_df["조합"])

    # 상위 3개 조합 추출
    top_3 = counter.most_common(3)

    # 결과 정리 (첫 번째 항목만 추출)
    result_dict = {}
    for i, (combo, _) in enumerate(top_3):
        순위 = f"{i+1}위"
        조합_리스트 = combo.split("-")
        result_dict[순위] = 조합_리스트[0] if len(조합_리스트) > 0 else "없음"

    # 부족한 경우 '없음'으로 채움
    for i in range(len(result_dict) + 1, 4):
        result_dict[f"{i}위"] = "없음"

    # 결과 출력
    print("✅ 예측 결과:", result_dict)

    # JSON 파일 저장
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump({"result": result_dict}, f, ensure_ascii=False)

    return result_dict

# 디버깅 시 단독 실행 가능
if __name__ == "__main__":
    run_prediction()
