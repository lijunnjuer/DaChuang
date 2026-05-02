from marshmallow import Schema, fields


class SpeciesSchema(Schema):
    id = fields.Int()
    common_name = fields.Str()
    scientific_name = fields.Str()
    trophic_level = fields.Str()
