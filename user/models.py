from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.conf import settings

class CustomUser(AbstractUser):
    profile_img = models.ImageField(upload_to=settings.IMAGE_UPLOAD_DIR.format(app_name="content", model_name="custom_user"), null=True, blank=True)
    description = RichTextField(blank=True)
    is_author = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

