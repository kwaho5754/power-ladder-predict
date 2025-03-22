import pandas as pd

# ✅ CSV 데이터 불러오기
filename = "power_ladder_data.csv"
df = pd.read_csv(filename)

# ✅ 변환 매핑 (문자 → 숫자)
mapping = {"좌삼짝": 0, "우삼홀": 1, "좌사홀": 2, "우사짝": 3}

# ✅ NaN 방지: '우사홀' → '우사짝' 변환
df.replace({"우사홀": "우사짝"}, inplace=True)

# ✅ 매핑 적용
df["결과1"] = df["결과1"].map(mapping)
df["결과2"] = df["결과2"].map(mapping)
df["결과3"] = df["결과3"].map(mapping)

# 🚨 NaN 발생 여부 확인
if df.isnull().sum().sum() > 0:
    print("🚨 NaN 값이 포함된 행 출력:")
    print(df[df.isnull().any(axis=1)])  # NaN 포함된 행 출력
else:
    print("✅ 모든 데이터 변환 성공! NaN 없음.")
