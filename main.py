# Imports that are used for the app
import os
from flask import Flask, config, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from werkzeug.wrappers import UserAgentMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from hashlib import sha256
import psycopg2
from wtforms import StringField, Form, validators, TextField, TextAreaField, SubmitField, PasswordField

# Creates Flask app
app = Flask(__name__)
app.config.from_object(__name__)
# Used to connect database on heroku to app
app.secret_key = os.environ.get('SECRET_KEY')
# The .replace() is used as a work around for heroku param error, not sure it it will be fixed on
# herokus end. If so, remove the .replace
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL').replace("://", "ql://", 1)
DATABASE_URL = os.environ['DATABASE_URL']

# Creates database using SQLAlchemy in the app
db = SQLAlchemy(app)

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

'''
This is the form used for the /form page and is called later in the code
'''


class ReusableForm(Form):
    owner = TextField('Owner: ', validators=[validators.required()])
    plant_species = TextField('Plant Species: ', validators=[
                              validators.required()])
    date_planted = TextField('Date Planted: ', validators=[
                             validators.required()])
    date_finish = TextField('Date Finished: ', validators=[
                            validators.required()])
    last_watered = TextField('Last Watered: ', validators=[
                             validators.required()])
    owner = TextField('Date PLanted: ', validators=[validators.required()])
    temp = TextField('Temperature: ', validators=[validators.required()])
    humidity = TextField('Humidity: ', validators=[validators.required()])
    soil_moisture = TextField('Soil Moisture: ', validators=[
                              validators.required()])
    bed = TextField('Bed Number: ', validators=[validators.required()])


'''
This is the structure that will be used in the database
'''


class Plants(db.Model):
    __tablename__ = "greenhouse"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plant_species = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    date_planted = db.Column(db.String(100), nullable=False)
    date_finish = db.Column(db.String(100), nullable=False)
    last_watered = db.Column(db.String(100), nullable=False)
    temp = db.Column(db.String(100), nullable=False)
    humidity = db.Column(db.String(100), nullable=False)
    soil_moisture = db.Column(db.String(100), nullable=False)
    bed = db.Column(db.String(100), nullable=False, primary_key=True)

    # Called to initialize the DB
    def __init__(self, plant_species, owner, date_planted, date_finish, last_watered, temp, humidity, soil_moisture, bed):
        self.plant_species = plant_species
        self.owner = owner
        self.date_planted = date_planted
        self.date_finish = date_finish
        self.last_watered = last_watered
        self.temp = temp
        self.humidity = humidity
        self.soil_moisture = soil_moisture
        self.bed = bed

    # Function that is called to produce DB row in jsonify

    def serialize(self):
        return{
            'bed': self.bed,
            'name': self.owner,
            'plant': self.plant_species,
            'date_planted': self.date_planted,
            'date_finished': self.date_finish,
            'last_watered': self.last_watered
        }

# Structure used for User DB


class User(db.Model):
    __tablename__ = "userCred"
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))


# Home route
@app.route('/')
def Home():
    return render_template('index.html', title='Home')

# Front route


@app.route('/front')
def Front():
    return render_template('front.html', title='Front')

# Back route


@app.route('/back')
def Back():
    return render_template('back.html')

# Outside route


@app.route('/outside')
def Outside():
    return render_template('outside.html')

# Used for the authentication page


@app.route('/auth', methods=["GET", "POST"])
def auth():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        # hash password
        hashword = sha256(password.encode('utf-8')).hexdigest()
        user = User.query.filter_by(name=name).first()
        if user is not None:
            if user.password == hashword and user.name == name:
                return render_template('UserAuth.html', flash_message="True")
            else:
                return render_template('UserAuth.html', flash_message="False")
        else:
            return render_template('UserAuth.html', flash_message="False")
    return render_template('UserAuth.html')

# Used for the bed contects page


@app.route('/bed-contents/<id_>')
def contents(id_):
    try:
        bed = Plants.query.filter_by(bed=id_).order_by(
            Plants._id.desc()).first()
        if bed != None:
            return render_template('bed-contents.html', bedNum=bed.bed, name=bed.owner, plant=bed.plant_species, date_planted=bed.date_planted, date_finished=bed.date_finish, last_watered=bed.last_watered)
        else:
            return render_template('bedErr.html', bedNum=id_)
    except Exception as e:
        return(str(e))

# Page for forms


@app.route('/form', methods=["GET", "POST"])
def form():
    form = ReusableForm(request.form)
    if request.method == 'POST':  # submit
        data = request.form  # data from the form
        date_planted = request.form['date_planted']
        plant_species = request.form['plant_species']
        owner = request.form['owner']
        date_finish = request.form['date_finish']
        last_watered = request.form['last_watered']
        temp = request.form['temp']
        humidity = request.form['humidity']
        soil_moisture = request.form['soil_moisture']
        bed = request.form['bed']
        new_data = Plants(plant_species, owner, date_planted, date_finish,
                          last_watered, temp, humidity, soil_moisture, bed)
        db.session.add(new_data)
        db.session.commit()

        user_data = Plants.query.all()
        return redirect('/')
    return render_template('testing.html', form=form, title='Planting Form')
