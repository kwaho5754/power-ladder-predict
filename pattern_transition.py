import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv("power_ladder_data.csv", encoding="utf-8")

# 특정 패턴이 다음 패턴으로 얼마나 이어지는지 저장할 딕셔너리
transition_counts = {col: {} for col in df.columns[1:]}  # '날짜' 제외

# 패턴 조합 계산
for column in df.columns[1:]:
    for i in range(len(df) - 1):  # 마지막 줄 제외
        current_pattern = df[column].iloc[i]  # 현재 패턴
        next_pattern = df[column].iloc[i + 1]  # 다음 패턴

        # 딕셔너리에 패턴 저장
        if current_pattern not in transition_counts[column]:
            transition_counts[column][current_pattern] = {}

        if next_pattern not in transition_counts[column][current_pattern]:
            transition_counts[column][current_pattern][next_pattern] = 0

        transition_counts[column][current_pattern][next_pattern] += 1  # 카운트 증가

# 확률 계산
for column in transition_counts:
    print(f"\n📌 [{column}] 패턴 조합 확률 (%)")
    for current_pattern in transition_counts[column]:
        total = sum(transition_counts[column][current_pattern].values())
        probs = {
            next_pattern: (count / total) * 100
            for next_pattern, count in transition_counts[column][current_pattern].items()
        }
        print(f"{current_pattern} → {probs}")
