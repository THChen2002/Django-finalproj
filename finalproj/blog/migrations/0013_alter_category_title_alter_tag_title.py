# Generated by Django 4.2.1 on 2023-06-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_remove_blogpost_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="tag",
            name="title",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
