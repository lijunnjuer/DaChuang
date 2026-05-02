from marshmallow import Schema, fields


class ApiResponseSchema(Schema):
    code = fields.Int(required=True)
    message = fields.Str(required=True)
    data = fields.Raw(required=True)
    timestamp = fields.Int()
    request_id = fields.Str()
