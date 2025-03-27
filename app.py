from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>파워사다리 예측 시스템</h2><p>/latest 또는 /run-predict로 이동하세요.</p>'

@app.route('/latest', methods=['GET'])
def latest():
    try:
        with open('latest_result.json', 'r', encoding='utf-8') as f:
            result = json.load(f)
        return f"""
        <h2>📊 최신 예측 결과</h2>
        <p>{result['result']}</p>
        """
    except FileNotFoundError:
        return "<p>아직 예측 결과가 없습니다.</p>"

@app.route('/run-predict', methods=['GET'])
def run_predict():
    try:
        result = subprocess.run(['python3', 'auto_predict.py'], capture_output=True, text=True)
        return f"<pre>{result.stdout}</pre>"
    except Exception as e:
    import traceback
    traceback.print_exc()
    return f"<p>예측 실행 중 오류 발생: {str(e)}</p>"

if __name__ == '__main__':
    app.run(debug=True)
