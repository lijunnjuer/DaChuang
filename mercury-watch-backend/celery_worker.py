from celery import Celery

celery_app = Celery("mercury_worker")
celery_app.conf.broker_url = "redis://redis:6379/0"
celery_app.conf.result_backend = "redis://redis:6379/1"


@celery_app.task(name="report.generate")
def generate_report_task(payload: dict):
    return {"status": "completed", "payload": payload}
