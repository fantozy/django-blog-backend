# Generated by Django 5.0.3 on 2024-03-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_topic_block'),
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='categories',
            field=models.ManyToManyField(blank=True, to='content.categories'),
        ),
    ]
