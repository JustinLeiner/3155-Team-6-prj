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
    my_post = db.session.query(get_post).filter_by(id=post_id).one() 
    my_image = Image.open("your_image_here");
    my_post + my_image.show()
    return redirect(url_for('index'))
