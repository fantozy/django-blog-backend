from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin
from .models import Menu, Block
from content.models import Topic

@admin.register(Menu)
class SortableBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

class TopicTabularInline(admin.TabularInline):
    model = Topic
    extra = 0

class BlockAdmin(admin.ModelAdmin):
    inlines = [TopicTabularInline]

admin.site.register(Block, BlockAdmin)


