from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'Power Ladder Prediction API is running!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # 예시 예측 로직 (실제 로직으로 교체 가능)
    result = {
        "result": "1위: 좌삼짝, 2위: 우삼홀, 3위: 좌사홀"
    }

    # 최신 결과를 파일로 저장
    with open('latest_result.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False)

    return jsonify(result)

@app.route('/latest', methods=['GET'])
def latest():
    try:
        with open('latest_result.json', 'r', encoding='utf-8') as f:
            result = json.load(f)
        return f"""
        <h2>🔮 최신 예측 결과</h2>
        <p>{result['result']}</p>
        """
    except FileNotFoundError:
        return "<p>아직 예측 결과가 없습니다.</p>"

if __name__ == '__main__':
    app.run(debug=True)
