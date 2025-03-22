@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # ✅ 1단계: 회차와 시간 정보 받기
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

    # ✅ 2단계: 결과 Google Sheet에 저장
    append_to_sheet(round_num, time_str, 좌삼짝, 우삼홀, 좌사홀, 우사짝)

    return jsonify({'result': prediction})

