from typing import List
from ninja import NinjaAPI, Query
from content.models import Topic, Categories
from modules.models import Block, Menu
from django.shortcuts import get_object_or_404

from modules.schemas import BlockSchema, MenuSchema, CategoriesSchema
from content.schemas import TopicFilterSchema, TopicSchema

api = NinjaAPI()


@api.get("/topics", response=List[TopicSchema])
def get_topic(request, filters: TopicFilterSchema = Query(...)):
    queryset = Topic.objects.all()
    filtered = filters.filter(queryset)

    return filtered

@api.post("/topics", response=TopicSchema)
def create_topic(request, topic_data: TopicSchema, author_id: int):
    topic_data_dict = topic_data.dict()
    topic_data_dict['author_id'] = author_id
    topic = Topic.objects.create(**topic_data_dict)
    return topic

@api.put("/topics/{topic_id}", response=TopicSchema)
def update_topic(request, topic_id: int, topic_data: TopicSchema):
    topic = Topic.objects.get(pk=topic_id)
    for key, value in topic_data.dict().items():
        setattr(topic, key, value)
    topic.save()

    return topic

@api.delete("/topics/{topic_id}", response=TopicSchema)
def delete_topic(request, topic_id: int):
    topic = get_object_or_404(Topic, pk=topic_id)
    topic.delete()
    
    return topic

@api.get("/blocks", response=List[BlockSchema])
def list_blocks(request):
    queryset = Block.objects.all()
    return queryset

@api.post("/blocks", response=BlockSchema)
def create_block(request, block_data: BlockSchema):
    block = Block.objects.create(**block_data.dict())
    
    return block

@api.put("/blocks/{block_id}", response=BlockSchema)
def update_block(request, block_id: int, block_data: BlockSchema):
    block = get_object_or_404(Block, pk=block_id)
    for key, value in block_data.dict().items():
        setattr(block, key, value)
    block.save()
    
    return block

@api.delete("/blocks/{block_id}", response=BlockSchema)
def delete_block(request, block_id: int):
    block = get_object_or_404(Block, pk=block_id)
    block.delete()
    
    return block

@api.get("/menus", response=List[MenuSchema])
def get_menu(request):
    queryset = Menu.objects.all()
    return queryset

@api.post("/menus", response=MenuSchema)
def create_menu(request, menu_data: MenuSchema):
    menu_data = menu_data.dict()
    menu = Menu.objects.create(**menu_data)
    return menu
 
@api.put("/menus/{menu_id}", response=MenuSchema)
def update_menu(request, menu_id: int, menu_data: MenuSchema):
    menu = get_object_or_404(Menu, pk=menu_id)
    for key, value in menu_data.dict().items():
        setattr(menu, key, value)
    menu.save()
    return menu

@api.delete("/menus/{menu_id}", response=MenuSchema)
def delete_menu(request, menu_id: int):
    menu = get_object_or_404(Menu,pk=menu_id)
    menu.delete()
    return menu

@api.get("/categories", response=List[CategoriesSchema])
def get_categories(request):
    categories = Categories.objects.all()
    return categories

@api.post("/categories", response=CategoriesSchema)
def create_category(request, category_data: CategoriesSchema):
    category_data.dict()
    category = Categories.objects.create(**category_data)
    return category

@api.put("/categories/{category_id}", response=CategoriesSchema)
def update_category(request, category_id: int, category_data: CategoriesSchema):
    category = get_object_or_404(Categories, pk=category_id)
    for key, value in category_data.dict().items():
        setattr(category, key, value)
    category.save()
    return category

@api.delete("/categories/{category_id}", response=CategoriesSchema)
def delete_category(request, category_id: int):
    category = get_object_or_404(pk=category_id)
    category.delete()
    return category
