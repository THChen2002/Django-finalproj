# Generated by Django 4.2.1 on 2023-06-12 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0013_alter_category_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="question",
            name="category",
        ),
        migrations.DeleteModel(
            name="Category",
        ),
        migrations.AddField(
            model_name="question",
            name="tag",
            field=models.ManyToManyField(to="quiz.tag"),
        ),
    ]