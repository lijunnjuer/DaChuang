from flask_restful import Resource


class RegionListResource(Resource):
    def get(self):
        return {"code": 200, "message": "region list placeholder", "data": []}
