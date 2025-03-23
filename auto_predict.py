import requests

url = "https://power-ladder-predict.onrender.com/predict"
headers = {"Content-Type": "application/json"}
data = {
    # 여기에 예측에 필요한 실제 데이터
}

response = requests.post(url, json=data, headers=headers, timeout=10)
print("예측 요청 완료:", response.text)
