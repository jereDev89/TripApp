from app import app , db
from flask import render_template, url_for, flash, redirect
from app.forms import LoginForm , RegisterForm , CreateTripForm
from app.models import User, Izlet , Kombinacija
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profil', username=current_user.username))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('index'))
        login_user(user)
        return redirect(url_for('profil', username=current_user.username))
    return render_template('index.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/registracija' , methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(ime_korisnika=form.ime_korisnika.data, email=form.email.data, mjesto_stanovanja=form.mjesto_stanovanja.data, username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('registracija.html', form=form)


@app.route('/profil/<username>')
@login_required
def profil(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profil.html', user=user)


@app.route('/dodajIzlet')
def dodajIzlet():
    return render_template('dodavanje_izleta.html')

@app.route('/izleti')
def izleti():
    return render_template('izlet.html')

@app.route('/popisIzleta')
def popisIzleta():
    return render_template('popis_izleta.html')
