from app import app
from flask import Flask, render_template, url_for, flash, redirect
from app.forms import LoginForm, CreateTripForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profil'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('profil'))
    return render_template('index.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/registracija')
def register():
    return render_template('registracija.html')


@app.route('/profil')
def profil():
    user = {
        'username': 'Jere',
        'ime_korisnika': 'Ivan Jeremic',
        'email': 'jere@gmail.com',
        'mjesto_stanovanja': 'Rijeka',
        'izleti_korisnika': 'bla bla'
    }
    return render_template('profil.html', user=user)


@app.route('/dodavanje_izleta', methods=['GET', 'POST'])
def dodaj():
    form = CreateTripForm()
    izlet = {
        'naziv_izleta': 'Rijeka',
        'lokacija': 'Rijeka',
        'datum': '28/01/2019',
        'minimalan': '1',
        'maksimalan': '51',
        'prijevoz': 'autobus',
        'opis': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
        'cijena': '200,00'
    }

    if form.validate_on_submit():
        return "Izlet dodan!"
    return render_template('dodavanje_izleta.html', title='Dodaj izlet', form=form)
