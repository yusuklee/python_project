import string
import random
from flask import Flask, request, redirect

# Flask 웹 서버 생성
app = Flask(__name__)

# 단축 URL과 원래 URL을 저장할 딕셔너리
url_mapping = {}

# 랜덤한 short_id(예: abc123) 생성 함수
def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits  # a-zA-Z0-9
    return ''.join(random.choices(characters, k=length))  # 예: 'xYz7A1'

# 사용자가 URL을 입력해서 단축 요청을 할 때 실행되는 함수
@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']  # HTML 폼에서 입력받은 URL

    # http:// 또는 https:// 안 써도 자동으로 http:// 붙여줌
    if not original_url.startswith(('http://', 'https://')):
        original_url = 'http://' + original_url

    # 이미 단축된 URL인지 확인
    for short_id, url in url_mapping.items():
        if url == original_url:
            return f"단축 URL: http://localhost:5000/{short_id}"

    # 고유한 short_id 생성
    short_id = generate_short_id()
    while short_id in url_mapping:
        short_id = generate_short_id()

    # short_id와 원래 URL 저장
    url_mapping[short_id] = original_url

    # 단축 URL 결과 출력
    return f"단축 URL: http://localhost:5000/{short_id}"

# 단축 URL로 들어왔을 때 원래 주소로 리디렉션하는 함수
@app.route('/<short_id>')
def redirect_to_url(short_id):
    original_url = url_mapping.get(short_id)  # 저장된 URL 꺼내오기
    if original_url:
        return redirect(original_url)  # 원래 주소로 이동
    return '존재하지 않는 단축 URL입니다.', 404

# 홈페이지: URL 입력 폼 보여주는 부분
@app.route('/')
def home():
    return '''
        <form action="/shorten" method="post">
            <input name="url" type="text" placeholder="URL 입력" required>
            <input type="submit" value="단축 URL 생성">
        </form>
    '''

# 서버 실행 (localhost:5000에서 작동)
if __name__ == '__main__':
    app.run(debug=True)
        