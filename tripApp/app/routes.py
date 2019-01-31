from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
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
    return render_template('index.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/registracija')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(ime_korisnika=form.ime.data, )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registracija.html', form=form)


@app.route('/profil/<username>')
@login_required
def profil(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profil.html', user=user)

    return render_template('profil.html')


@app.route('/dodajIzlet')
def dodajIzlet():

    return render_template('dodavanje_izleta.html')
