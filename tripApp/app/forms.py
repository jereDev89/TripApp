
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, DateField, DecimalField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    ime = StringField('Ime', validators=[DataRequired()])
    submit = SubmitField('Registriraj se!')


class CreateTripForm(FlaskForm):
    naziv_izleta = StringField('Naziv_izleta', validators=[DataRequired()])
    lokacija = StringField('Lokacija', validators=[DataRequired()])
    datum = DateField('Datum', validators=[DataRequired()])
    minimalan = StringField('Min_broj_sudionika', validators=[DataRequired()])
    maksimalan = StringField('Max_broj_sudionika', validators=[DataRequired()])
    prijevoz = StringField('Prijevoz', validators=[DataRequired()])
    opis = StringField('Opis_izleta', validators=[DataRequired()])
    cijena = DecimalField('Cijena', validators=[DataRequired()])
    dodaj = SubmitField('dodaj_izlet')
