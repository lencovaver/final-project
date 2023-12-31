# Generated by Django 4.2.2 on 2023-06-28 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("jobapp", "0013_postjob_language_alter_postjob_experience"),
    ]

    operations = [
        migrations.CreateModel(
            name="Language",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name="postjob",
            name="language",
        ),
        migrations.CreateModel(
            name="LanguageLevel",
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
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("A1", "A1"),
                            ("A2", "A2"),
                            ("B1", "B1"),
                            ("B2", "B2"),
                            ("C1", "C1"),
                            ("C2", "C2"),
                        ],
                        default="A1",
                        max_length=100,
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jobapp.language",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="postjob",
            name="languages",
            field=models.ManyToManyField(
                related_name="postjobs", to="jobapp.languagelevel"
            ),
        ),
    ]
