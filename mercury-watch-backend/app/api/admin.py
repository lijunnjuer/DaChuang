from flask_restful import Resource


class AdminPingResource(Resource):
    def get(self):
        return {"code": 200, "message": "admin module placeholder", "data": {"status": "ok"}}
