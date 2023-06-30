# Generated by Django 4.2.2 on 2023-06-28 20:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobapp", "0012_alter_postjob_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="postjob",
            name="language",
            field=models.CharField(
                choices=[
                    ("ENG", "🇬🇧 english"),
                    ("DEU", "🇩🇪 germany"),
                    ("FRA", "🇫🇷 french"),
                    ("ITA", "🇮🇹 italy"),
                    ("CHF", "🇨🇭 swiss german"),
                    ("NO", "none"),
                ],
                default="none",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="postjob",
            name="experience",
            field=models.CharField(
                choices=[
                    ("1-3", "1-3 years"),
                    ("4-6", "4-6 years"),
                    ("6-9", "6-9 years"),
                    ("10+", "10 years and more"),
                ],
                default="1-3",
                max_length=100,
            ),
        ),
    ]