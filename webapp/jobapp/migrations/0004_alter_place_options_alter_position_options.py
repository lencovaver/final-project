# Generated by Django 4.2.2 on 2023-06-27 20:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("jobapp", "0003_alter_postjob_positions"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="place",
            options={"ordering": ["name_place"]},
        ),
        migrations.AlterModelOptions(
            name="position",
            options={"ordering": ["name_position"]},
        ),
    ]
