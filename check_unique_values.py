import pandas as pd

# ✅ CSV 데이터 불러오기
filename = "power_ladder_data.csv"
df = pd.read_csv(filename)

# ✅ '결과1' 컬럼에서 변환되지 않은 값 확인
print("🚨 변환되지 않은 고유값 리스트:")
print(df["결과1"].unique())  # 중복 제거된 모든 값 출력
