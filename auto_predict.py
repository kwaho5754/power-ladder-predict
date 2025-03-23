import requests

url = "https://power-ladder-predict.onrender.com/predict"
headers = {"Content-Type": "application/json"}
data = {}

try:
    response = requests.post(url, headers=headers, json=data)
    print("예측 요청 완료:", response.text)
except Exception as e:
    print("에러 발생:", e)
