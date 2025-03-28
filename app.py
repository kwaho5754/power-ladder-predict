from flask import Flask, request, jsonify
import subprocess
import json
import traceback

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
        <h2>✅ 최신 예측 결과</h2>
        <p>1위: {result['result']['1위']}</p>
        <p>2위: {result['result']['2위']}</p>
        <p>3위: {result['result']['3위']}</p>
        """
    except FileNotFoundError:
        return "<p>아직 예측 결과가 없습니다.</p>"

@app.route('/run-predict', methods=['GET'])
def run_predict():
    try:
        result = subprocess.run(['python', 'auto_predict.py'], capture_output=True, text=True)
        with open('latest_result.json', 'r', encoding='utf-8') as f:
            latest = json.load(f)
        return f"""
        <h2>✅ 예측 실행 완료</h2>
        <p>예측 결과:</p>
        <p>1위: {latest['result']['1위']}</p>
        <p>2위: {latest['result']['2위']}</p>
        <p>3위: {latest['result']['3위']}</p>
        """
    except Exception as e:
        return f"<p>❌ 예측 실행 중 오류 발생:<br>{str(e)}<br><br>{traceback.format_exc()}</p>"

if __name__ == '__main__':
    app.run(debug=True)
