# Generated by Django 4.2.2 on 2023-07-09 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_alter_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='num',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='company',
            name='street',
            field=models.CharField(default='', max_length=255),
        ),
    ]
