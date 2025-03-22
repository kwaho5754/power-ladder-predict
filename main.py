from waitress import serve
from app import app  # 여전히 app.py가 존재한다면 app.py에서 app을 가져옵니다.

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
