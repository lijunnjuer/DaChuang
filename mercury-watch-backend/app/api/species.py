from flask_restful import Resource


class SpeciesListResource(Resource):
    def get(self):
        return {"code": 200, "message": "species list placeholder", "data": []}


class SpeciesDetailResource(Resource):
    def get(self, species_id: int):
        return {"code": 200, "message": "species detail placeholder", "data": {"id": species_id}}


class SpeciesSearchResource(Resource):
    def get(self):
        return {"code": 200, "message": "species search placeholder", "data": []}


class SpeciesCategoriesResource(Resource):
    def get(self):
        return {"code": 200, "message": "species categories placeholder", "data": []}
