import pandas as pd

# 기존 데이터 불러오기
df = pd.read_csv("power_ladder_data.csv", encoding="utf-8")

# 새로운 데이터 생성 예제 (실제 코드를 적용해야 함)
new_data = pd.DataFrame([["2025-03-19", "좌삼짝", "우삼홀", "좌사홀"]], columns=df.columns)

# 중복 확인 및 저장
if df.merge(new_data, how="inner").empty:
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv("power_ladder_data.csv", index=False, encoding="utf-8")
    print("✅ 새로운 데이터 추가됨!")
else:
    print("⚠️ 중복 데이터, 추가하지 않음.")
