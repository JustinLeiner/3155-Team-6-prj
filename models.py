from database import db

class Note(db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    title = db.Column("title", db.String(200))
    text = db.Column("text", db.String(100))
    date = db.Column("date", db.String(50))
    likes = db.Column("like", db.Integer)
    dislikes = db.Column("dislike", db.Integer)

    def __init__(self, title, text, date, likes, dislikes):
        self.title = title
        self.text = text
        self.date = date
        self.likes = likes
        self.dislikes = dislikes

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email 
