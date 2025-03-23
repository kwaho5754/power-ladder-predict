from flask import Flask, request, jsonify
from append_prediction import append_to_sheet

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    round_num = data.get("round")
    time_str = data.get("time")
    좌삼짝 = data.get("좌삼짝")
    우삼홀 = data.get("우삼홀")
    좌사홀 = data.get("좌사홀")
    우사짝 = data.get("우사짝")

    # 아주 간단한 예측 로직
    if 좌삼짝 == "짝" and 우삼홀 == "홀":
        prediction = "예측결과: 1위"
    else:
        prediction = "예측결과: 2위"

    # 구글 시트에 저장
    append_to_sheet(round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝)

    return jsonify({"result": prediction})
