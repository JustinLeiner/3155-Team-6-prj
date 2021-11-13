import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
from flask import redirect, url_for
from database import db
from models import Note as Note
from models import User as User


# delete post #
@app.route('/notes/delete/<note_id>', methods = ['Note'])
def delete_note(note_id):
    #retrieve note from database
    my_note = db.session.query(Note).filter_by(id=note_id).one()
    db.session.delete(my_note)
    db.session.commit()

    return redirect(url_for('get_notes'))









