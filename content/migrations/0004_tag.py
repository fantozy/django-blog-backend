# Generated by Django 5.0.3 on 2024-03-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_categories_depth_categories_numchild_categories_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=320)),
            ],
        ),
    ]