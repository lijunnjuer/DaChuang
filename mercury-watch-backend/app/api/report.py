from flask_restful import Resource


class ReportGenerateResource(Resource):
    def post(self):
        return {
            "code": 200,
            "message": "report generation placeholder",
            "data": {"task_id": "placeholder-task", "status": "pending"}
        }


class ReportStatusResource(Resource):
    def get(self, task_id: str):
        return {
            "code": 200,
            "message": "report status placeholder",
            "data": {"task_id": task_id, "status": "processing", "progress": 0}
        }


class ReportDownloadResource(Resource):
    def get(self, file_id: str):
        return {
            "code": 200,
            "message": "report download placeholder",
            "data": {"file_id": file_id, "url": ""}
        }
