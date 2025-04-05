from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm): #flaskform 상속
    username = StringField('Username',validators=[DataRequired(), Length(min=3)]) #input생성 라벨은 User~~
    password = PasswordField('Password', validators=[DataRequired(),Length(min=4)])
    submit = SubmitField('등록')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('로그인')