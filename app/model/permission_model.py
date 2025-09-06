from app import db
from datetime import datetime
import pytz
from sqlalchemy import Enum


def ist_now():
    return datetime.now(pytz.timezone("Asia/Kolkata"))


class Permission(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    reason = db.Column(db.String(255))
    from_ = db.Column(db.Date)
    to = db.Column(db.Date)
    description = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=ist_now)
    user = db.relationship("User", backref="permission")
    status = db.Column(
        Enum("Pending", "Approved", "Rejected", name="status_enum"), default="Pending"
    )
