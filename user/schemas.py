from ninja import Schema, FilterSchema, Field
from typing import Optional

class CustomUserFilterSchema(FilterSchema):
    pk: Optional[int] = Field(None, q="pk")

class CustomUserSchema(Schema):
    description: str
    is_author: bool
    email: str
    username: str


