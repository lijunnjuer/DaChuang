from marshmallow import Schema, fields


class ReportTaskSchema(Schema):
    task_id = fields.Str()
    status = fields.Str()
    file_url = fields.Str()
