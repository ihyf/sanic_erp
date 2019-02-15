from tortoise import fields
from .base import BaseModel


class User(BaseModel):
    username = fields.CharField(max_length=20)
    password = fields.CharField(max_length=100)
    status = fields.IntField(default=1)
    
    class Meta:
        table = 'user'


