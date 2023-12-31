# Generated by Django 4.2.2 on 2023-06-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobapp", "0011_postjob_experience_alter_postjob_salary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postjob",
            name="experience",
            field=models.CharField(
                choices=[
                    ("1-3", "1-3 roky"),
                    ("4-6", "4-6 roky"),
                    ("6-9", "6-9 let"),
                    ("10+", "10 let a více"),
                ],
                default="1-3",
                max_length=100,
            ),
        ),
    ]
