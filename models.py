from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Appointment {self.specialty} on {self.date} in {self.location}>'

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(20))
    level = db.Column(db.String(20))
    description = db.Column(db.Text)
    image = db.Column(db.String(200))

    def __repr__(self):
        return f'<Exercise {self.name} ({self.category})>'

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(200))
    link = db.Column(db.String(200))

    def __repr__(self):
        return f'<Category {self.name}>'

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    channel = db.Column(db.String(100))
    duration = db.Column(db.String(20))
    thumbnail = db.Column(db.String(200))

    def __repr__(self):
        return f'<Video {self.title}>'