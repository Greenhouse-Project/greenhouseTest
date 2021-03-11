import os  
from flask import Flask,render_template

app = Flask(__name__)

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
    
# # Outside route
# @app.route('/outside')
# def Outside():
#     return 'The Outside Room Page works'
#     # return render_template('TBD', title='Outside')
    
# # About route
# @app.route('/about')
# def About():
#     return 'The About page is working'
# #     return render_template('TBD', title='About')