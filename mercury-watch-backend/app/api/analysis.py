from flask_restful import Resource


class BiomagnificationResource(Resource):
    def get(self):
        return {"code": 200, "message": "biomagnification placeholder", "data": {}}


class YearlyStatsResource(Resource):
    def get(self):
        return {"code": 200, "message": "yearly stats placeholder", "data": {}}


class RegionRankingResource(Resource):
    def get(self):
        return {"code": 200, "message": "region ranking placeholder", "data": []}


class ExportResource(Resource):
    def post(self):
        return {"code": 200, "message": "export placeholder", "data": {}}
