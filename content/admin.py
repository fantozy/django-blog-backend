from django.contrib import admin

from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Categories, Tag, Topic

class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Categories)

admin.site.register(Categories, MyAdmin)
admin.site.register(Tag)
admin.site.register(Topic)

