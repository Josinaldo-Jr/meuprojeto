from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TelField, TextAreaField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, Length, Regexp
from flask_wtf.csrf import CSRFProtect

class Contato(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    phone = TelField('phone', validators=[DataRequired()])
    message = TextAreaField('message')
    submit = SubmitField('submit')

class Cadastro(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    submit = SubmitField('submit')

    # novos campos para o cadastro
    cpf = StringField('CPF', validators=[DataRequired()])
    phone = TelField('phone', validators=[DataRequired()])
    street = StringField('street address (with number)', validators=[DataRequired()])
    neighborhood = StringField('neighborhood', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    state = SelectField('state address', choices=[
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    ], validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])