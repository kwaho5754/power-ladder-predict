import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv("power_ladder_data.csv", encoding="utf-8")

# 연속 패턴 개수를 저장할 딕셔너리
continuous_counts = {col: [] for col in df.columns[1:]}  # '날짜' 제외

# 연속된 패턴 개수 계산
for column in df.columns[1:]:
    previous = None
    count = 0

    for value in df[column]:
        if value == previous:
            count += 1
        else:
            if previous is not None:
                continuous_counts[column].append(count)
            count = 1  # 새로운 패턴 등장
        previous = value

# 결과 출력
for column in continuous_counts:
    print(f"\n📌 [{column}] 연속된 패턴 개수 분포")
    print(pd.Series(continuous_counts[column]).value_counts().sort_index())
