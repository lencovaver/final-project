# Generated by Django 4.2.2 on 2023-07-09 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_user_options_alter_city_name_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
