# Generated by Django 4.1.7 on 2023-04-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_userprofile_occupation"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="academic",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
