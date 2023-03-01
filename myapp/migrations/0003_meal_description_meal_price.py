# Generated by Django 4.1.7 on 2023-03-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='description',
            field=models.TextField(default='delicious'),
        ),
        migrations.AddField(
            model_name='meal',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
