from ninja import Schema
from typing import List, Optional

class CategoriesSchema(Schema):
    path: str
    depth: int
    name: str

class TagSchema(Schema):
    name: str
    
    
class BlockSchema(Schema):
    visual: str
    position: str
    order: int
    title: str
    show_title: bool

class MenuSchema(Schema):
    name: str
    url_field: str
    is_external: bool
    categories: Optional[List[int]] = None
    is_active: bool