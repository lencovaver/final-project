# Generated by Django 4.2.2 on 2023-07-01 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_useragent_user_userperson_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_useragent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_userperson',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='useragent',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='useragent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userperson',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userperson', to=settings.AUTH_USER_MODEL),
        ),
    ]
