# Generated by Django 4.2.1 on 2023-05-07 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_alter_userprofile_profile_pic"),
        ("blog", "0006_alter_blogpost_publish_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="BoardUnitResponse",
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
                ("bresponse", models.TextField(blank=True, default="")),
                ("bresponse_time", models.DateTimeField(blank=True, null=True)),
                (
                    "bresponse_author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.userprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BoardUnit",
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
                ("btime", models.DateTimeField(auto_now_add=True)),
                ("bcontent", models.TextField()),
                (
                    "bauthor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.userprofile",
                    ),
                ),
                (
                    "bblogpost",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.blogpost"
                    ),
                ),
            ],
        ),
    ]