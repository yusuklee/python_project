import string
import random
from flask import Flask, request, redirect

app = Flask(__name__)

url_mapping = {}

def make_short_id():
    characters = string.ascii_letters+string.digits
    return ''.join(random.choices(characters,k=4))

@app.route('/short',methods = ['POST'])
def shorten_url():
    original = request.form['url']

    if not original.startswith(('http://','https://')):
        original='https://'+original

    
    for short_id, url in url_mapping.items():
        if url==original:
            return f'단축URL=> https://localhost:5000/{short_id}'
        
    short_id=make_short_id()
    while short_id in url_mapping:
        short_id = make_short_id()

    url_mapping[short_id]=original

    return f'단축URL=> https://localhost:5000/{short_id}'

@app.route('/<short_id>')
def redirect_to_original(short_id): 
    if url_mapping.get(short_id): 
        return redirect(url_mapping[short_id])
    return '존재하지 않는 단축 url임'
        

@app.route('/')
def home():
     return '''
        <form action="/short" method="post">
            <input name="url" type="text" placeholder="URL 입력" required>
            <input type="submit" value="단축 URL 생성">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)