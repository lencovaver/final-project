# Generated by Django 4.2.3 on 2023-07-11 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobapp', '0026_alter_drivinglicence_licence'),
    ]

    operations = [
        migrations.AddField(
            model_name='postjob',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
