from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import LoginForm


@app.route('/')
@app.route('/index' , methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect('/profil')
    return render_template('index.html', form=form)



    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)



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
