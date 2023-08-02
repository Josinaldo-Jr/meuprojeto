from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class Contato(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    phone = TelField('phone', validators=[DataRequired()])
    message = TextAreaField('message')
    submit = SubmitField('submit')