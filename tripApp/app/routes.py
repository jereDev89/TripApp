from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def login():
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('index'))
        return redirect('profil')


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
        'username': 'Jere' ,
        'ime_korisnika': 'Ivan Jeremic' ,
        'email': 'jere@gmail.com' ,
        'mjesto_stanovanja': 'Rijeka' ,
        'izleti_korisnika': 'bla bla'
        }
    return render_template('profil.html' , user=user)
