from flask_restful import Resource


class MercuryByRegionResource(Resource):
    def get(self):
        return {"code": 200, "message": "by-region placeholder", "data": {}}


class MercuryBySpeciesResource(Resource):
    def get(self, species_id: int):
        return {"code": 200, "message": "by-species placeholder", "data": {"id": species_id}}


class MercuryCompareResource(Resource):
    def post(self):
        return {"code": 200, "message": "compare placeholder", "data": {}}


class MercuryTemporalSpatialResource(Resource):
    def get(self):
        return {"code": 200, "message": "temporal-spatial placeholder", "data": {}}
