# Generated by Django 4.2.1 on 2023-05-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0011_remove_quizresultdetail_user_answer_time_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="correct_rate",
            field=models.FloatField(default=0),
        ),
    ]