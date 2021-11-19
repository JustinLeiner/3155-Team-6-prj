import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
from flask import request
from flask import redirect, url_for
from database import db
from models import Note as Note
from models import User as User
from flask import Image

@app.route('/notes/attach image/<note_id>', methods = ['Note'])
def attach_image(note_id):
my_note = db.session.query(Note).filter_by(id=note_id).one()
note_id = my_note;
my_Image = Image.open("your_image_here");
my_note + my_Image.show();
