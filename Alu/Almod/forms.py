from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,ValidationError,DataRequired
from flask_wtf import FlaskForm
class LoginForm(FlaskForm):
    username=StringField(label='Username',validators=[Length(min=4),DataRequired()])
    password=PasswordField(label='Password',validators=[Length(min=4),DataRequired()])
    login=SubmitField(label='Login')
