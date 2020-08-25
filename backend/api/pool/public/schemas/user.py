from marshmallow import fields

from backend.common.schemas import BaseCreatingSchema


class UserSchema(BaseCreatingSchema):
    id = fields.String(required=True)
