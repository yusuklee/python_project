from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy() #주로 클래스를 데이터베이스와 연결하는 객체

class User(db.Model): #Model 클래스를 상속받으면 데이터베이스 테이블과 매핑됨
    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    