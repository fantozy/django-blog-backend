from django.db import models
from content.models import Categories

class Menu(models.Model):
    name = models.CharField(max_length=250)
    is_external = models.BooleanField(default=False)
    categories = models.ManyToManyField(Categories, blank=True)
    is_active = models.BooleanField(default=True)
    url_field = models.URLField()

    class Meta:
        ordering = ['name']

class Block(models.Model):
    class VisualChoices(models.TextChoices):
        STANDARD = 'ST', 'Standard'
        HORIZONTAL = 'HR', 'Horizontal'
        VERTICAL = 'VR', 'Vertical'
    visual = models.CharField(max_length=2, choices=VisualChoices.choices, default=VisualChoices.STANDARD)
    position = models.CharField(max_length=50)
    order = models.IntegerField()
    title = models.CharField(max_length=250)
    show_title = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)