from marshmallow import Schema, fields

class RegisterSchema(Schema):
    name = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)

class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

class UserResponseSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    name = fields.String()