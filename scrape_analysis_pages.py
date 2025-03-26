import requests
from bs4 import BeautifulSoup

# 크롤링할 URL들
URLS = {
    "일별 분석": "https://ntry.com/stats/power_ladder/date.php",
    "회차 분석": "https://ntry.com/stats/power_ladder/round.php",
    "패턴 분석": "https://ntry.com/stats/power_ladder/pattern.php"
}

def scrape_table(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr') if table else []

    result = []
    for row in rows:
        cols = [col.get_text(strip=True) for col in row.find_all(['td', 'th'])]
        if cols:
            result.append(cols)
    return result

if __name__ == "__main__":
    for name, url in URLS.items():
        print(f"\n▶ {name} 결과")
        table_data = scrape_table(url)
        for row in table_data[:5]:  # 처음 5줄만 미리보기
            print(row)
