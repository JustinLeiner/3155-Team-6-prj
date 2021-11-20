import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for
from database import db
from models import Note as Note
from models import User as User
from flask import Image

@app.route('/post/attach image/<post_id>', methods = ['POST'])
def attach_image(post_id):
    if session.get('user_id'):
        if request.method =='POST':
            image = request.form['image']
            post_id = random.randint(10000, 99999)
            post = db.session.query(Note).filter_by(id=post_id).first()
            Post = post_id
            user = User.query.filter_by(username = username).first()
            UserName = user.username
            <input type="file" name="datafile" size="40">
            try:
                input type ="file" accept="image/*" /
                thisrecord = Posts(post_id, title, image, post_id, userName)
                db.session.add(thisrecord)
                db.session.commit()
                return redirect(url_for('image', username =username, post=id))
            except:

                posts = db.session.query(Note).all()
                print(post)
                print(postsOut)
        else:
            user_a = User.query.filter_by(username=username).first()
            post = db.session.query(Note).filter_by(id=post_id).first()
            return render_template('image.html', user = user_a)
    else:
        return redirect(url_for('login'))
