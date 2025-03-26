import pandas as pd
from bs4 import BeautifulSoup
import requests

# 공통 함수 정의
def fetch_table_data(url, table_index=0):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    if not tables or table_index >= len(tables):
        return None
    table = tables[table_index]

    headers = [th.text.strip() for th in table.find_all('th')]
    rows = []
    for tr in table.find_all('tr')[1:]:
        cols = [td.text.strip() for td in tr.find_all('td')]
        if cols:
            rows.append(cols)

    return pd.DataFrame(rows, columns=headers) if rows else None

# URL 정의
daily_url = 'https://ntry.com/stats/power_ladder/date.php'
round_url = 'https://ntry.com/stats/power_ladder/round.php'
pattern_url = 'https://ntry.com/stats/power_ladder/pattern.php'

# 데이터 수집
daily_df = fetch_table_data(daily_url)
round_df = fetch_table_data(round_url)
pattern_df = fetch_table_data(pattern_url)

# 결과 출력 (미리보기)
print("[✔] 일별 분석 미리보기:")
print(daily_df.head(), "\n")

print("[✔] 회차 분석 미리보기:")
print(round_df.head(), "\n")

print("[✔] 패턴 분석 미리보기:")
print(pattern_df.head())
