from typing import Optional, List
from ninja import FilterSchema, Field, Schema

class TopicFilterSchema(FilterSchema):
    pk: Optional[int] = Field(None, q="pk")
    category_id: Optional[int] = Field(None, q="categories__id__eq")
    tag: Optional[str] = Field(None, q="tags__name__icontains")

class TopicSchema(Schema):
    topic_name: str
    description: str
    categories: Optional[List[int]] = None
    tags: Optional[List[int]] = None
    block: Optional[int] = None

