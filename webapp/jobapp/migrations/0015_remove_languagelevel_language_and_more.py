# Generated by Django 4.2.2 on 2023-06-28 21:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobapp", "0014_language_remove_postjob_language_languagelevel_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="languagelevel",
            name="language",
        ),
        migrations.RemoveField(
            model_name="postjob",
            name="languages",
        ),
        migrations.AddField(
            model_name="postjob",
            name="language",
            field=models.CharField(
                choices=[
                    ("NO", "none"),
                    ("ENG", "🇬🇧 english"),
                    ("CHF", "🇨🇭 swiss german"),
                    ("DEU", "🇩🇪 germany"),
                    ("FRA", "🇫🇷 french"),
                    ("ITA", "🇮🇹 italy"),
                ],
                default="NO",
                max_length=100,
            ),
        ),
        migrations.DeleteModel(
            name="Language",
        ),
        migrations.DeleteModel(
            name="LanguageLevel",
        ),
    ]
