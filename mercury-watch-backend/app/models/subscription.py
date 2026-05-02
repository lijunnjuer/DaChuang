from datetime import datetime

from app import db


class Subscription(db.Model):
    __tablename__ = "subscription"

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(128), index=True)
    subscribe_type = db.Column(db.String(20))
    target_id = db.Column(db.Integer, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
