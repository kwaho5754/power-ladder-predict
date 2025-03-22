import pandas as pd

filename = "power_ladder_data.csv"

df = pd.read_csv(filename, encoding="utf-8")

# 🔴 **중복 제거**
df = df.drop_duplicates().reset_index(drop=True)

# 정리된 CSV 파일 다시 저장
df.to_csv(filename, encoding="utf-8", index=False)

print(f"✅ 중복 제거 완료! 최신 데이터는 아래와 같습니다:\n")
print(df)
