# Generated by Django 4.2.1 on 2023-05-06 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounts", "0008_alter_userprofile_profile_pic"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("category", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
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
                ("question", models.CharField(max_length=500, unique=True)),
                (
                    "question_url",
                    models.ImageField(
                        blank=True, null=True, upload_to="question_pics/"
                    ),
                ),
                ("choice1", models.CharField(max_length=150)),
                ("choice2", models.CharField(max_length=150)),
                ("choice3", models.CharField(max_length=150)),
                ("choice4", models.CharField(max_length=150)),
                (
                    "question_type",
                    models.CharField(
                        choices=[
                            ("Multiple Choice", "Multiple Choice"),
                            ("True or False", "True or False"),
                        ],
                        max_length=50,
                    ),
                ),
                ("question_level", models.IntegerField()),
                ("correct_answer", models.CharField(max_length=50)),
                ("detail_explanation", models.TextField(blank=True, null=True)),
                (
                    "explanation_url",
                    models.ImageField(
                        blank=True, null=True, upload_to="explanation_pics/"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="quiz.category"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Quiz",
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
                ("quiz_name", models.CharField(max_length=50)),
                ("quiz_description", models.TextField(blank=True, null=True)),
                ("quiz_questions", models.ManyToManyField(to="quiz.question")),
            ],
        ),
        migrations.CreateModel(
            name="QuizResult",
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
                ("score", models.IntegerField()),
                (
                    "quiz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="quiz.quiz"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="accounts.userprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QuizResultDetail",
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
                ("user_answer", models.CharField(max_length=50)),
                ("correct", models.BooleanField(default=False)),
                ("choice1_selected", models.IntegerField()),
                ("choice2_selected", models.IntegerField()),
                ("choice3_selected", models.IntegerField()),
                ("choice4_selected", models.IntegerField()),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="quiz.question"
                    ),
                ),
                (
                    "quiz_result",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="quiz.quizresult",
                    ),
                ),
            ],
        ),
    ]
