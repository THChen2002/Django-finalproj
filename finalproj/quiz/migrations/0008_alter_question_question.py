# Generated by Django 4.2.1 on 2023-05-11 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0007_alter_question_explanation_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="question",
            field=models.CharField(max_length=500),
        ),
    ]