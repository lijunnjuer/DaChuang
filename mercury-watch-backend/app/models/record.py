from app import db


class MercuryRecord(db.Model):
    __tablename__ = "mercury_record"

    id = db.Column(db.Integer, primary_key=True)
    species_id = db.Column(db.Integer, db.ForeignKey("species.id"), index=True)
    concentration = db.Column(db.Numeric(10, 6), nullable=False)
    sampling_year = db.Column(db.Integer, index=True)
    geom = db.Column(db.String(255))
    organ = db.Column(db.String(20))
    stage = db.Column(db.String(20))
    std_dev = db.Column(db.Numeric(10, 6))
    reference_id = db.Column(db.Integer, index=True)
    continent = db.Column(db.String(10), index=True)
    iso_code = db.Column(db.String(5), index=True)
    common_name_cache = db.Column(db.String(100))
    risk_level_cache = db.Column(db.String(10))
