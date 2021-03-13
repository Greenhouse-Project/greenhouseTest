import os  
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hmcjtyhcsvdyvp:ae7e4a3535fa02d0a51c50d52357d7434b0ce16dd3d8caee2887adbce643d35c@ec2-54-159-175-113.compute-1.amazonaws.com:5432/d5s3splm4psiqk'

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
@app.route('/testing')
def Testing():
    return render_template('testing.html', title='Testing') 