# Generated by Django 4.2.3 on 2023-07-18 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0033_remove_drivinglicence_licence_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivinglicence',
            name='short_name',
            field=models.CharField(default='', max_length=3),
        ),
    ]
