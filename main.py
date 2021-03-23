import os 
from boto.s3.connection import S3Connection
from flask import Flask, config,render_template,request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, Form,validators, TextField, TextAreaField, SubmitField

# Creates Flask app
app = Flask(__name__)

app.secret_key= S3Connection(os.environ['SECRET_KEY'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hmcjtyhcsvdyvp:ae7e4a3535fa02d0a51c50d52357d7434b0ce16dd3d8caee2887adbce643d35c@ec2-54-159-175-113.compute-1.amazonaws.com:5432/d5s3splm4psiqk'

# Creates database using SQLAlchemy in the app
db = SQLAlchemy(app)

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
    _id = db.Column(db.Integer, primary_key=True)
    plant_species = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    date_planted = db.Column(db.String(100), nullable=False)
    date_finish = db.Column(db.String(100), nullable=False)
    last_watered = db.Column(db.String(100), nullable=False)
    temp = db.Column(db.String(100), nullable=False)
    humidity = db.Column(db.String(100), nullable=False)
    soil_moisture = db.Column(db.String(100), nullable=False)
    bed = db.Column(db.String(100), nullable=False, primary_key=True)

    def __init__(self, plant_species, owner,date_planted, date_finish, last_watered, temp, humidity, soil_moisture, bed):
        self.plant_species = plant_species
        self.owner = owner
        self.date_planted = date_planted
        self.date_finish = date_finish
        self.last_watered = last_watered
        self.temp = temp
        self.humidity = humidity
        self.soil_moisture = soil_moisture
        self.bed = bed
        

# Home route
@app.route('/')
def Home():
    return render_template('index.html', title='Home')

# Outside route
@app.route('/outside')
def Outside():
    return 'The Outside Room Page works'
    # return render_template('TBD', title='Outside')
    
# About route
@app.route('/about')
def About():
    return 'The About page is working'
#     return render_template('TBD', title='About')

# Page for forms
@app.route('/form', methods = ["GET", "POST"])
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
        return render_template('testing.html', user_data = user_data)
    if form.validate():
        flash('Hello ' + form)
    else:
        flash('All form fields are required')
    return render_template('testing.html',form = form, title='Planting Form') 