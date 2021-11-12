import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
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
    a_user = db.session.query(User).filter_by(email='jleiner1@uncc.edu').one()

    user_posts = db.session.query(Note).all()

   # print(new_post)
    return render_template('home.html', posts = user_posts, user=a_user)

# new post template #
@app.route('/new_question', methods = ['GET', 'POST'])
def new_post():
    if request.method== 'POST':

        title = request.form['questiontitle']

        text = request.form['newquestion']

         # Create date stamp
        from datetime import date
        today = date.today()

        # Date format
        today = today.strftime("%m-%d-%Y")

        new_record = Note(title, text, today)

        db.session.add(new_record)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        a_user = db.session.query(User).filter_by(email='jleiner1@uncc.edu').one()
        return render_template('new_question.html', user=a_user)


app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)