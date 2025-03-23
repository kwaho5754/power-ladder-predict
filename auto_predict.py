import requests

url = "https://power-ladder-predict.onrender.com/predict"

try:
    response = requests.get(url)
    print("예측 요청 완료:", response.text)
except Exception as e:
    print("에러 발생:", e)
