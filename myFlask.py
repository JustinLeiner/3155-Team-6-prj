import os  # os is used to get environment variables IP & PORT
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for
from database import db
from models import Note as Note
from models import User as User
from forms import RegisterForm
from forms import LoginForm
from flask import session
import bcrypt
from models import Comment as Comment
from forms import CommentForm

app = Flask(__name__)  # create an app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_note_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'SE3155'
#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)
# Setup models
with app.app_context():
    db.create_all()  # run under the app context


# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page

# Home page #
@app.route('/')
@app.route('/home/', methods=['GET', 'POST'])
def index():
    if session.get('user_id'):

        # retrieve posts( called notes in database) from database
        posts = db.session.query(Note).all()

        return render_template('home.html', user=session['user_id'], posts=posts)
    else:
        return render_template('home.html')


@app.route('/<post_id>')
def get_post(post_id):
    if session.get('user_id'):

        user_post = db.session.query(Note).filter_by(id=post_id).one()
        form = CommentForm()

        return render_template('selected_question.html', post=user_post, user=session['user_id'], form=form)
    else:
        return redirect(url_for('login'))


# new post template #
@app.route('/new_question', methods=['GET', 'POST'])
def new_post():
    if session.get('user_id'):
        if request.method == 'POST':

            title = request.form['questiontitle']

            text = request.form['newquestion']
            likes = 0
            dislikes = 0;
            # Create date stamp
            from datetime import date
            today = date.today()

            # Date format
            today = today.strftime("%m-%d-%Y")

            new_record = Note(title, text, today, session['user_id'], likes, dislikes)

            db.session.add(new_record)
            db.session.commit()

            return redirect(url_for('index'))
        else:
            return render_template('new_question.html', user=session['user_id'])
    else:
        return redirect(url_for('login'))


@app.route('/edit/<post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    if session.get('user_id'):
        # check method used for request
        if request.method == 'POST':
            # get title data
            title = request.form['title']
            # get post data
            text = request.form['noteText']
            post = db.session.query(Note).filter_by(id=post_id).one()
            # update post data
            post.title = title
            post.text = text
            # update post in DB
            db.session.add(post)
            db.session.commit()

            return redirect(url_for('index'))
        else:
            # GET request - show new post form to edit post
            # retrieve post from database
            my_post = db.session.query(Note).filter_by(id=post_id).one()

            return render_template('edit_selected_question.html', post=my_post, user=session['user_id'])
    else:
        return redirect(url_for('login'))


@app.route('/home/delete/<post_id>', methods=['POST'])
def delete_post(post_id):
    if session.get('user_id'):
        # retrieve post from database
        user_post = db.session.query(Note).filter_by(id=post_id).one()
        db.session.delete(user_post)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        # salt and hash password
        h_password = bcrypt.hashpw(
            request.form['password'].encode('utf-8'), bcrypt.gensalt())
        # create user model
        new_user = User(request.form['email'], h_password)
        # add user to database and commit
        db.session.add(new_user)
        db.session.commit()
        # save the user's name to the session
        session['user_id'] = new_user.id  # access id value from user model of this newly added user
        # show user dashboard view
        return redirect(url_for('index'))

    # something went wrong - display register view
    return render_template('register.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    # validate_on_submit only validates using POST
    if login_form.validate_on_submit():
        # we know user exists. We can use one()
        the_user = db.session.query(User).filter_by(email=request.form['email']).one()
        # user exists check password entered matches stored password
        if bcrypt.checkpw(request.form['password'].encode('utf-8'), the_user.password):
            # password match add user info to session
            session['user_id'] = the_user.id
            # render view
            return redirect(url_for('index'))

        # password check failed
        # set error message to alert user
        login_form.password.errors = ["Incorrect username or password."]
        return render_template("login.html", form=login_form)
    else:
        # form did not validate or GET request
        return render_template("login.html", form=login_form)


@app.route('/logout')
def logout():
    # check if user is logged in
    if session.get('user_id'):
        session.clear()
    return redirect(url_for('index'))

@app.route('/posts/<post_id>/dislikes', methods['POST'])
def like(post_id, action):
    if session.get('user'):
        post = db.session.query(Question).filter_by(id=post_id).one()

        likes = post.likes
        likes = likes + 1
        post.likes = likes

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('get_post', question_id=post_id))
    else:
        return redirect(url_for('login'))

@app.route('/posts/<post_id>/dislikes', methods['POST'])
def dislike(post_id, action):
    if session.get('user'):
        post = db.session.query(Question).filter_by(id=post_id).one()

        dislikes = post.dislikes
        dislikes = dislikes + 1
        post.dislikes = dislikes

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('get_post', question_id=post_id))
    else:
        return redirect(url_for('login'))


@app.route('/home/<post_id>/comment', methods=['POST'])
def new_comment(post_id):
    if session.get('user_id'):
        comment_form = CommentForm()
        # validate_on_submit only validates using POST
        if comment_form.validate_on_submit():
            # get comment data
            comment_text = request.form['comment']
            new_record = Comment(comment_text, int(post_id), session['user_id'])
            db.session.add(new_record)
            db.session.commit()

        return redirect(url_for('get_post', post_id=post_id))

    else:
        return redirect(url_for('login'))


app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)
