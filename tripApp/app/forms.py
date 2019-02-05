
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, DateField, DecimalField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    ime_korisnika = StringField('Ime', validators=[DataRequired()])
    email = StringField('Email' , validators=[DataRequired()])
    mjesto_stanovanja = StringField('Mjesto stanovanja')
    username = StringField('Username' , validators=[DataRequired()])
    password = PasswordField('Password' , validators=[DataRequired()])
    # password_repeat = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password_hash')])
    submit = SubmitField('Registracija')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username vec postoji...')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email adresa vec postoji...')


class CreateTripForm(FlaskForm):
    naziv_izleta = StringField('Naziv_izleta', validators=[DataRequired()])
    lokacija = StringField('Lokacija', validators=[DataRequired()])
    datum = DateField('Datum', validators=[DataRequired()])
    min_broj_sudionika = StringField('Min_broj_sudionika', validators=[DataRequired()])
    max_broj_sudionika = StringField('Max_broj_sudionika', validators=[DataRequired()])
    prijevoz = StringField('Prijevoz', validators=[DataRequired()])
    opis_izleta = StringField('Opis_izleta', validators=[DataRequired()])
    cijena = DecimalField('Cijena', validators=[DataRequired()])
    dodaj = SubmitField('dodaj_izlet')
