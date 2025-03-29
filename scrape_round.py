import requests
from bs4 import BeautifulSoup

def get_current_round():
    url = "https://ntry.com/scores/power_ladder/live.php"
    try:
        response = requests.get(url, timeout=5)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')

        # 수정된 구조에 맞게 찾기 (예: span.tit 또는 다른 요소)
        round_tag = soup.select_one("span.tit")
        if round_tag:
            return round_tag.text.strip()
        else:
            return "알 수 없음"
    except Exception:
        return "알 수 없음"

if __name__ == "__main__":
    print(get_current_round())
