from marshmallow import Schema, fields


class MercuryRecordSchema(Schema):
    id = fields.Int()
    species_id = fields.Int()
    concentration = fields.Float()
    sampling_year = fields.Int()
