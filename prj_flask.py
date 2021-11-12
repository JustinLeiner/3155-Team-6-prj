# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
import os
import re                 # os is used to get environment variables IP & PORT  # Flask is the web app that we will customize
from flask import Flask 
from flask import render_template
from flask import request
from flask import redirect, url_for 
from database import db
from models import Note as Note
from models import User as User

app = Flask(__name__)     # create an app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_note_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)
# Setup models
with app.app_context():
    db.create_all()   # run under the app context


# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page

# Home page #
@app.route('/')
@app.route('/home', methods = ['GET', 'POST'])
def index():
    return render_template('home.html', new_post = new_post)

# new post template #
@app.route('/new_question', methods = ['GET', 'POST'])
def new_post():
    if request.method== 'POST':

        title = request.form['questionTitle']

        text = request.form['newQuestion']

        new_record = Note(title, text)

        db.session.add(new_record)
        db.session.commit()

        return redirect(url_for('home.html'))
    else:

        return render_template('new_question.html')


app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)

# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# Note that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.