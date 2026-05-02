from datetime import datetime

from app import db


class Species(db.Model):
    __tablename__ = "species"

    id = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String(100), nullable=False, index=True)
    scientific_name = db.Column(db.String(100), nullable=False)
    trophic_level = db.Column(db.String(10), index=True)
    production_mode = db.Column(db.String(20))
    isscaap_0 = db.Column(db.Integer)
    isscaap_1 = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
