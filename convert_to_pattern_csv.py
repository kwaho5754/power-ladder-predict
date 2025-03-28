import pandas as pd

# 기존 파일 불러오기
df = pd.read_csv("powerladder_data.csv")

# 결과값 기준으로 조합 열 만들기
def extract_patterns(row):
    result = row['결과']
    patterns = {
        '좌삼짝': int(result == '좌삼짝'),
        '우삼홀': int(result == '우삼홀'),
        '좌사홀': int(result == '좌사홀'),
        '우사짝': int(result == '우사짝')
    }
    return pd.Series(patterns)

# 새 컬럼 추가
new_df = df.apply(extract_patterns, axis=1)

# 결과 CSV 저장
new_df.to_csv("powerladder_data.csv", index=False, encoding='utf-8-sig')
print("✅ 변환 완료! powerladder_data.csv 새로 저장됨.")
