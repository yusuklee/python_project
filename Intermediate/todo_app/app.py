from flask import Flask, render_template, redirect, url_for, request, session, flash
from models import db, User, Todo
from forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'todo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

db.init_app(app)

with app.app_context(): 
    db.create_all() #플라스크앱에 데이터베이스 테이블 만들려면 이리함

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    #query는 데이터베이스 검색할때 시작점
    todos = Todo.query.filter_by(user_id=session['user_id']).order_by(Todo.created_at.desc()).all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    content = request.form.get('content')
    if content:
        new_todo = Todo(content=content, user_id=session['user_id'])
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('index'))
    

@app.route('/toggle/<int:todo_id>')
def toggle(todo_id):
    todo = Todo.qeury.get_or_404(todo_id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/login', methods = ['GET', 'POST']) #/login으로 접속하거나 폼을 제출할때 실행되는 함수
def login():
    form = LoginForm()
    if form.validate_on_submit(): #폼이 조건을 통과하고 제출됬을때
        user = User.query.filter_by(username = form.username.data).first() #User 테이블에서 폼에 알맞은 유저를 가져옴
        if user and check_password_hash(user.password, form.password.data): #해시된 비번과 사용자가 입력한 비밀번호가 같은지 확인
            session['user_id']= user.id #같으면 세션의 userid에 유저의 아이디 저장
            return redirect(url_for('index')) #todo list로 이동
    else: flash('Invalid credentials') #조건을 통과하지 못했을때
    return render_template('login.html', form = form) #조건 통과못하고 다시 로그인창으로 이동
    

@app.route('/register',methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)#사용자가 준 비번을 해시로 바꾸는것
        user =User(username = form.username.data,password=hashed_pw)
        db.session.add(user) #데이터베이스 연결세션임 flask세션과는 다름
        db.session.commit()#데이터베이스에 연결한후에 추가한후에 저장
        return redirect(url_for('login'))
    return render_template('register.html',form=form)#회원정보를 제데로 입력안했을때 제자리

@app.route('/logout')
def logout():
    session.pop('user_id',None)
    return redirect(url_for('login'))

if __name__ =='__main__':
    app.run(debug=True)