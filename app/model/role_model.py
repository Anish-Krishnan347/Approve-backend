from app import db
from datetime import datetime
import pytz

def ist_now():
    return datetime.now(pytz.timezone("Asia/Kolkata"))

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=ist_now)
