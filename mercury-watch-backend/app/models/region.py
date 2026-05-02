from app import db


class Region(db.Model):
    __tablename__ = "region"

    id = db.Column(db.Integer, primary_key=True)
    iso_code = db.Column(db.String(5), unique=True, index=True)
    admin_region = db.Column(db.String(50))
    continent = db.Column(db.String(10), index=True)
    center_geom = db.Column(db.String(255))
    ecosystem_category = db.Column(db.String(50))
