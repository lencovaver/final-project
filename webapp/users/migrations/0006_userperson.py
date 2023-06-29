# Generated by Django 4.2.2 on 2023-06-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_useragent"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserPerson",
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
                ("name", models.CharField(max_length=50)),
                ("surname", models.CharField(max_length=50)),
                ("phone", models.IntegerField(default="no_number")),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
