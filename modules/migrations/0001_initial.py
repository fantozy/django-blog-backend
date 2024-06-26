# Generated by Django 5.0.3 on 2024-03-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0005_alter_categories_logos_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visual', models.CharField(choices=[('ST', 'Standard'), ('HR', 'Horizontal'), ('VR', 'Vertical')], default='ST', max_length=2)),
                ('position', models.CharField(max_length=50)),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=250)),
                ('show_title', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('is_external', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('categories', models.ManyToManyField(blank=True, null=True, to='content.categories')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
