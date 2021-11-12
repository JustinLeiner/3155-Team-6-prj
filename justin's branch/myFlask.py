import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
from flask import request

app = Flask(__name__)     # create an app

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

        return redirect(url_for('home.html'))


    return render_template('new_question.html')


app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)