import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# CSV 파일 불러오기
filename = "power_ladder_data.csv"
df = pd.read_csv(filename, encoding="utf-8")

# 문자열 데이터를 숫자로 변환 (Label Encoding)
encoder = LabelEncoder()
for column in ["결과1", "결과2", "결과3"]:
    df[column] = encoder.fit_transform(df[column])

# 훈련 데이터와 테스트 데이터 나누기
X = df[["결과1", "결과2"]]
y = df["결과3"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 변환된 데이터 확인
print("훈련 데이터 샘플:\n", X_train.head())
print("테스트 데이터 샘플:\n", X_test.head())
