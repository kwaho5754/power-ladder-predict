import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv("power_ladder_data.csv", encoding="utf-8")

# 각 패턴별 빈도수 계산
for column in df.columns[1:]:  # '날짜' 컬럼 제외하고 분석
    print(f"\n📌 [{column}] 결과별 빈도수")
    print(df[column].value_counts())  # 각 값이 나온 횟수
