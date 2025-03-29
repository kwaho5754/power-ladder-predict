from flask import Flask
import json
import traceback
from auto_predict import run_prediction

app = Flask(__name__)

@app.route("/")
def index():
    return "<h2>파워사다리 예측 시스템</h2><p>/run-predict 또는 /latest로 이동하세요.</p>"

@app.route("/run-predict")
def run_predict():
    try:
        result = run_prediction()
        return f"""
        <h2>✅ 예측 실행 완료</h2>
        <p>예측 결과:</p>
        <p>현재 회차: {result.get("회차", "알 수 없음")}</p>
        <p>1위: {result.get("1위", "없음")}</p>
        <p>2위: {result.get("2위", "없음")}</p>
        <p>3위: {result.get("3위", "없음")}</p>
        """
    except Exception as e:
        return f"<p>❌ 예측 실행 중 오류 발생:<br>{str(e)}<br><br>{traceback.format_exc()}</p>"

@app.route("/latest")
def latest():
    try:
        with open("latest_result.json", "r", encoding="utf-8") as f:
            result = json.load(f)["result"]
        return f"""
        <h2>✅ 최신 예측 결과</h2>
        <p>현재 회차: {result.get("회차", "알 수 없음")}</p>
        <p>1위: {result.get("1위", "없음")}</p>
        <p>2위: {result.get("2위", "없음")}</p>
        <p>3위: {result.get("3위", "없음")}</p>
        """
    except FileNotFoundError:
        return "<p>예측 결과 파일이 없습니다.</p>"
