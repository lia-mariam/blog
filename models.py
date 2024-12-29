from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class Post(db.Model):
   
    id = db.Column(db.Integer, primary_key=True)  #primary key
    title = db.Column(db.String(100), nullable=False)  # Title column
    content = db.Column(db.Text, nullable=False)  # Content column
    author = db.Column(db.String(50), nullable=False)  # Author column
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Date column

    def serialize(self):
        return {
            'id':self.id,
            'title':self.title,
            'content':self.content,
            'author':self.author,
            'date_posted':self.date_posted.strftime('%Y-%m-%d %H:%M:%S')
        }

