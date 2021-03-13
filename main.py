import os  
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hmcjtyhcsvdyvp:ae7e4a3535fa02d0a51c50d52357d7434b0ce16dd3d8caee2887adbce643d35c@ec2-54-159-175-113.compute-1.amazonaws.com:5432/d5s3splm4psiqk'

db = SQLAlchemy(app)

class Plants(db.model):
    __tablename__ = "greenhouse"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plant_species = db.Column(db.String(100), nullable=False)
    owner = db.Column(db.String(100), nullable=False)
    date_finish = db.Column(db.String(100), nullable=False)
    last_watered = db.Column(db.String(100), nullable=False)
    temp = db.Column(db.String(100), nullable=False)
    humidity = db.Column(db.String(100), nullable=False)
    soil_moisture = db.Column(db.String(100), nullable=False)
    bed = db.Column(db.String(100), nullable=False)

    def __init__(self, plant_species, owner, date_finish, last_watered, temp, humidity, soil_moisture, bed):
        self.plant_species = plant_species
        self.owner = owner
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
    
# # Front Room route
# @app.route('/front-room')
# def FrontRoom():
#     return 'The Front Room Page works'
#     # return render_template('TBD', title='Front Room')
    
# # Back Room route
# @app.route('/back-room')
# def BackRoom():
#     return 'The Back Room Page works'
#     # return render_template('TBD', title='Back Room')
    
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

# Testing page for forms
@app.route('/testing', methods = ["GET", "POST"])
def Testing():
    if request.method == 'POST': # submit
        data= request.form # data from the form
        plant_species = data["plant_species"]
        owner = data["owner"]
        date_finish = data["date_finish"]
        last_watered = data["last_watered"]
        temp = data["temp"]
        humidity = data["humidity"]
        soil_moisture = data["soil_moisture"]
        bed = data["bed"]
        new_data = Plants(plant_species, owner, date_finish, last_watered, temp, humidity, soil_moisture, bed)
        db.session.add(new_data)
        db.session.commit()
        
        user_data = Plants.query.all()
        return render_template('testing.html', user_data = user_data)
    return render_template('testing.html', title='Testing') 