import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

# CSV 파일 불러오기
filename = "power_ladder_data.csv"
df = pd.read_csv(filename)

# ✅ 변환 매핑 정의
mapping = {
    "좌삼짝": 0, "우삼홀": 1, "우삼짝": 2, "좌사홀": 3,
    "우사짝": 4, "우사홀": 5, "좌사짝": 6
}

# ✅ 변환되지 않은 값 확인
print("🔵 [1단계] 변환되지 않은 고유 값 확인")
for col in ["결과1", "결과2", "결과3"]:
    unique_values = df[col].unique()
    not_converted = [val for val in unique_values if val not in mapping]
    if not_converted:
        print(f"  결과 {col} 변환되지 않은 값: {not_converted}")

# ✅ 매핑 적용
for col in ["결과1", "결과2", "결과3"]:
    df[col] = df[col].replace(mapping)

# ✅ 변환 후 데이터 확인
print("\n✅ [2단계] 변환된 데이터 확인")
print(df.head())

# ✅ NaN 값 확인 및 처리 (NaN이 있으면 0으로 채움)
if df.isnull().values.any():
    print("\n⚠ NaN 값이 발견되었습니다. 0으로 대체합니다.")
    df.fillna(0, inplace=True)

# ✅ 데이터 타입 변환
df[["결과1", "결과2", "결과3"]] = df[["결과1", "결과2", "결과3"]].astype(int)

# ✅ 변환 확인
print("\n🔴 데이터 타입 확인")
print(df.dtypes)

# ✅ 학습 데이터 준비
X = df[["결과1", "결과2"]].values  # 입력값
y = df["결과3"].values  # 예측 대상

# ✅ 모델 학습
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# ✅ 모델 저장
with open("power_ladder_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\n✅ 모델 학습 완료 & 저장됨: power_ladder_model.pkl")
