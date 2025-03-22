import pandas as pd

# 기존 데이터 로드
filename = "power_ladder_data.csv"
try:
    df = pd.read_csv(filename)
except FileNotFoundError:
    df = pd.DataFrame(columns=["날짜", "결과1", "결과2", "결과3"])

# 새 데이터 수집 (여기에 실제 스크래핑한 데이터를 넣어야 함)
new_data = pd.DataFrame([["2025-03-19", "좌삼짝", "우삼홀", "좌사홀"]], columns=df.columns)

# 중복 데이터 제거 후 추가
if not df.isin(new_data.values).all(axis=1).any():
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print("✅ 데이터가 추가되었습니다!")
else:
    print("⚠ 중복 데이터, 추가하지 않음.")
