from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    ime_korisnika = db.Column(db.String(120), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    mjesto_stanovanja = db.Column(db.String(120), index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Izlet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naziv_izleta = db.Column(db.String(140))
    lokacija = db.Column(db.String(140))
    datum = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    min_broj_sudionika = (db.Integer)
    max_broj_sudionika = (db.Integer)
    prijevoz = db.Column(db.Text(140))
    opis_izleta = db.Column(db.Text(140))
    cijena = db.Column(db.Float)

    def __repr__(self):
        return '<Izlet {}>'.format(self.naziv_izleta)

class Kombinacija(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    izlet_id = db.Column(db.Integer, db.ForeignKey('izlet.id'))

    def __repr__(self):
        return '<Kombinacija {}>'.format(self.user_id , self.izlet_id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))