from flask import Flask
import sys

app = Flask(__name__)

# 커맨드라인 인자로 포트 번호 입력받기
port = sys.argv[1] if len(sys.argv) > 1 else '5000'

@app.route('/')
def index():
    return f'Port : {port}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port))
