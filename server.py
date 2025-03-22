from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# 최근 10개 데이터 저장
data_list = []

@app.route('/update_data', methods=['POST'])
def update_data():
    """ 크롤러에서 전송한 데이터를 저장 """
    global data_list
    new_data = request.json.get("data", {})

    if new_data:
        data_list.append(new_data)
        data_list = data_list[-10:]  # 최근 10개만 유지
        print("서버에 저장된 데이터:", data_list)

    return jsonify({"status": "success", "data": data_list})

@app.route('/get_data', methods=['GET'])
def get_data():
    """ 저장된 데이터 반환 """
    return jsonify({"data": data_list})

@app.route('/predict', methods=['GET'])
def predict():
    """ 간단한 예측: 최근 3개 데이터를 기준으로 가장 많이 나온 값 예측 """
    if len(data_list) >= 3:
        last_three = [d["odd_even"] for d in data_list[-3:]]  # 최근 3개 데이터에서 홀짝 값 가져오기
        prediction = max(set(last_three), key=last_three.count)  # 가장 많이 나온 값 예측
    else:
        prediction = "데이터 부족"

    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
v