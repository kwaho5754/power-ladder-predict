import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv("power_ladder_data.csv", encoding="utf-8")

# 각 패턴별 발생 확률 계산
for column in df.columns[1:]:  # '날짜' 컬럼 제외
    print(f"\n📌 [{column}] 결과별 발생 확률 (%)")
    print(df[column].value_counts(normalize=True) * 100)  # 백분율로 변환
