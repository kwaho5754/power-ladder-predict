import pandas as pd

# CSV 파일 읽기
df = pd.read_csv("powerladder_data.csv", encoding="utf-8-sig")

# 데이터 출력
print(df)
