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
    db.create_all()

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
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

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id']= user.id
            return redirect(url_for('index'))
        flash('Invalid credentials')
    return render_template('login.html', form = form)
    

@app.route('/register',methods = ['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user =User(username = form.username.data,password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

@app.route('/logout')
def logout():
    session.pop('user_id',None)
    return redirect(url_for('login'))

if __name__ =='__main__':
    app.run(debug=True)