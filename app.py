from flask import Flask, request, jsonify
from append_prediction import append_to_sheet  # ← 이 줄도 꼭 있어야 해!

app = Flask(__name__)  # ← 가장 먼저 app 선언이 되어야 함

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # 데이터 추출
    round_num = data.get("round")
    time_str = data.get("time")
    좌삼짝 = data.get("좌삼짝")
    우삼홀 = data.get("우삼홀")
    좌사홀 = data.get("좌사홀")
    우사짝 = data.get("우사짝")

    # 예측 로직
    if 좌삼짝 == "짝" and 우삼홀 == "홀":
        prediction = "예측결과: 1위"
    else:
        prediction = "예측결과: 2위"

    # 구글 시트에 저장
    append_to_sheet(round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝)

    return jsonify({'result': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
