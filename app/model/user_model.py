from app import db
from datetime import datetime
from sqlalchemy import Boolean,Enum
import pytz

def ist_now():
    return datetime.now(pytz.timezone("Asia/Kolkata"))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email=db.Column(db.String(75))
    password = db.Column(db.String(20))
    role_id=db.Column(db.Integer,db.ForeignKey('role.id'))
    role = db.relationship('Role', backref='users')
    status = db.Column(Enum('active', 'inactive', name='status_enum'), default='active')
    approve = db.Column(Boolean, default=False)
    created_at = db.Column(db.DateTime, default=ist_now)
    
