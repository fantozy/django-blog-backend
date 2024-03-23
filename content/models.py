from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from treebeard.mp_tree import MP_Node

class Categories(MP_Node):
    path = models.CharField(max_length=255, unique=True, null=True, blank=True)
    depth = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=250)
    logos = models.ImageField(upload_to=settings.IMAGE_UPLOAD_DIR.format(app_name="content", model_name="categories"), null=True, blank=True)
    parent = models.ForeignKey("self", on_delete = models.CASCADE, null=True, blank=True)

class Tag(models.Model):
    name = models.CharField(max_length=320)

class Topic(models.Model):
    topic_name = models.CharField(max_length=500)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    author = models.ForeignKey("user.CustomUser", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categories)
    tags = models.ManyToManyField(Tag)
    main_picture = models.ImageField(upload_to=settings.IMAGE_UPLOAD_DIR.format(app_name="content", model_name="topics"), null=True, blank=True)
    published = models.BooleanField(default=True)
    block = models.ForeignKey("modules.block", on_delete=models.CASCADE, null=True, blank=True)



