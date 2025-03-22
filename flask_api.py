from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API is running!"

# /predict 엔드포인트 추가 (POST 요청 허용)
@app.route("/predict", methods=["POST"])  # << POST 요청 허용
def predict():
    data = request.get_json()  # JSON 데이터 받기
    left_side = data.get("left_side", 0)
    right_side = data.get("right_side", 0)

    # 간단한 예측 로직 (예제)
    prediction = left_side + right_side

    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
