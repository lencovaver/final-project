# Generated by Django 4.2.2 on 2023-07-09 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_useragent_area_code_alter_userperson_area_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_userperson',
        ),
    ]
