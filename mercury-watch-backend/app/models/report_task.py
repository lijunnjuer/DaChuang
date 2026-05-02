from datetime import datetime

from app import db


class ReportTask(db.Model):
    __tablename__ = "report_task"

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.String(64), unique=True, index=True)
    status = db.Column(db.String(20), index=True)
    file_url = db.Column(db.String(500))
    params = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    completed_at = db.Column(db.DateTime)
