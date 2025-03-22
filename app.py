from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # 예: data = {"좌삼짝": "짝", "우삼홀": "홀", "좌사홀": "홀", "우사짝": "짝"}
    좌삼짝 = data.get('좌삼짝')
    우삼홀 = data.get('우삼홀')
    좌사홀 = data.get('좌사홀')
    우사짝 = data.get('우사짝')

    # 아주 간단한 테스트용 예측 로직 (나중에 머신러닝 모델로 교체)
    if 좌삼짝 == '짝' and 우삼홀 == '홀':
        prediction = '예측결과: 1위'
    else:
        prediction = '예측결과: 2위'

    return jsonify({'result': prediction})

if __name__ == '__main__':
    from os import environ
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
