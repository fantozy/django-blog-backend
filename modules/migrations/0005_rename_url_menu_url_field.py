# Generated by Django 5.0.3 on 2024-03-22 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0004_alter_menu_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='url',
            new_name='url_field',
        ),
    ]
