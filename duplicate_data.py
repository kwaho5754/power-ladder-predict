import pandas as pd

# 기존 CSV 파일 불러오기
filename = "power_ladder_data.csv"
df = pd.read_csv(filename, encoding="utf-8")

# 데이터 복사하여 30배 증가
df = pd.concat([df] * 30, ignore_index=True)

# 저장
df.to_csv(filename, index=False, encoding="utf-8-sig")
print("✅ 데이터가 30배 증가되었습니다!")
