# Generated by Django 5.0.3 on 2024-03-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_customuser_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='static/content/custom_user/images'),
        ),
    ]
