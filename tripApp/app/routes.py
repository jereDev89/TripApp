from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse


@app.route('/')
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

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('index.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/registracija')
def register():
    return render_template('registracija.html')


@app.route('/profil')
def profil():

    return render_template('profil.html')


@app.route('/dodajIzlet')
def dodajIzlet():

    return render_template('dodavanje_izleta.html')
