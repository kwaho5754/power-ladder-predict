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

    # 간단한 규칙 기반 순위 예측
    scores = {
        "좌삼짝": 0.0,
        "우삼홀": 0.0,
        "좌사홀": 0.0,
        "우사짝": 0.0
    }

    if 좌삼짝 == "짝":
        scores["좌삼짝"] += 1
    if 우삼홀 == "홀":
        scores["우삼홀"] += 1
    if 좌사홀 == "홀":
        scores["좌사홀"] += 1
    if 우사짝 == "짝":
        scores["우사짝"] += 1

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    rank_1 = sorted_scores[0][0]
    rank_2 = sorted_scores[1][0]
    rank_3 = sorted_scores[2][0]

    prediction = f"1위: {rank_1}, 2위: {rank_2}, 3위: {rank_3}"

    # 구글 시트에 저장
    append_to_sheet(round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝, rank_1, rank_2, rank_3)

    return jsonify({"result": prediction})
