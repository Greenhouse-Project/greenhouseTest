import os 
from flask import Flask, config,render_template,request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from werkzeug.wrappers import UserAgentMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm

from sqlalchemy.ext.hybrid import hybrid_property
import psycopg2
from wtforms import StringField, Form,validators, TextField, TextAreaField, SubmitField, PasswordField

# Creates Flask app
app = Flask(__name__)
app.config.from_object(__name__)

app.secret_key= os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
DATABASE_URL = os.environ['DATABASE_URL']

# Creates database using SQLAlchemy in the app
db = SQLAlchemy(app)

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

class ReusableForm(Form):
    owner = TextField('Owner: ', validators=[validators.required()])
    plant_species = TextField('Plant Species: ', validators=[validators.required()])
    date_planted = TextField('Date Planted: ', validators=[validators.required()])
    date_finish = TextField('Date Finished: ', validators=[validators.required()])
    last_watered = TextField('Last Watered: ', validators=[validators.required()])
    owner = TextField('Date PLanted: ', validators=[validators.required()])
    temp = TextField('Temperature: ', validators=[validators.required()])
    humidity = TextField('Humidity: ', validators=[validators.required()])
    soil_moisture = TextField('Soil Moisture: ', validators=[validators.required()])
    bed = TextField('Bed Number: ', validators=[validators.required()])
    
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
    
    
    @hybrid_property
    def password(self):
        self._password
    
    def __init__(self, plant_species, owner,date_planted, date_finish, last_watered, temp, humidity, soil_moisture, bed, _password):
        self.plant_species = plant_species
        self.owner = owner
        self.date_planted = date_planted
        self.date_finish = date_finish
        self.last_watered = last_watered
        self.temp = temp
        self.humidity = humidity
        self.soil_moisture = soil_moisture
        self.bed = bed
        
    def serialize(self):
        return{
            'bed': self.bed,
            'name': self.owner,
            'plant': self.plant_species,
            'date_planted': self.date_planted,
            'date_finished': self.date_finish,
            'last_watered' : self.last_watered
        }
        
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

@app.route('/auth', methods=["POST"])
def auth():
    name = request.form.get('name')
    password = request.form.get('password')
    
    user = User.query.filter_by(name=name).first()
    
    if not user or not check_password_hash(user.password, password):
        flash('Incorrect login. Please try again.')
        return redirect('/form')
    
    return render_template('UserAuth.html')
    
@app.route('/bed-contents/<id_>')
def contents(id_):
    try:
        bed = Plants.query.filter_by(bed=id_).order_by(Plants._id.desc()).first()
        if bed != None:
            return render_template('bed-contents.html',bedNum=bed.bed, name=bed.owner, plant=bed.plant_species, date_planted=bed.date_planted, date_finished=bed.date_finish, last_watered=bed.last_watered)
        else:
            return render_template('bedErr.html', bedNum=id_)
    except Exception as e:
        return(str(e))

# Page for forms
@app.route('/form', methods = ["GET", "POST"])
@login_required
def form():
    form = ReusableForm(request.form)
    if request.method == 'POST': # submit
        data= request.form # data from the form
        date_planted = request.form['date_planted']
        plant_species = request.form['plant_species']
        owner = request.form['owner']
        date_finish = request.form['date_finish']
        last_watered = request.form['last_watered']
        temp = request.form['temp']
        humidity = request.form['humidity']
        soil_moisture = request.form['soil_moisture']
        bed = request.form['bed']
        new_data = Plants(plant_species, owner,date_planted, date_finish, last_watered, temp, humidity, soil_moisture, bed)
        db.session.add(new_data)
        db.session.commit()
        
        user_data = Plants.query.all()
        return redirect('/')
    return render_template('testing.html',form = form, title='Planting Form') 