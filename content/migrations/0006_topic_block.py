# Generated by Django 5.0.3 on 2024-03-22 12:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_alter_categories_logos_topic'),
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modules.block'),
        ),
    ]
