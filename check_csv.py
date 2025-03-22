import pandas as pd

# CSV 파일 로드
filename = "power_ladder_data.csv"
df = pd.read_csv(filename)

# 🔹 변환할 값 매핑 설정 (check_csv에서도 적용)
mapping = {
    "좌삼짝": 0,
    "우삼홀": 1,
    "좌사홀": 2,
    "우사짝": 3,
    "우삼짝": 4,
    "우사홀": 5
}

# 🔹 매핑 적용
df[["결과1", "결과2", "결과3"]] = df[["결과1", "결과2", "결과3"]].replace(mapping)

# 🔹 CSV 미리보기
print("📄 CSV 데이터 미리보기:")
print(df.head(10))

# 🔹 고유값 확인
print("🔵 날짜의 고유 값:", df["날짜"].unique())
print("🔵 결과1의 고유 값:", df["결과1"].unique())
print("🔵 결과2의 고유 값:", df["결과2"].unique())
print("🔵 결과3의 고유 값:", df["결과3"].unique())

# 🔹 NaN 값 확인
print("\n⚠ NaN 값 개수:")
print(df.isnull().sum())
