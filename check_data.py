import pandas as pd  # Pandas 라이브러리 불러오기

# CSV 파일 불러오기
df = pd.read_csv("power_ladder_data.csv", encoding="utf-8")

# 데이터 확인 (앞부분 5개 출력)
print(df.head())
