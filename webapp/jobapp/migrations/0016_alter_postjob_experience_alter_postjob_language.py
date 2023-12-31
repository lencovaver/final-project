# Generated by Django 4.2.2 on 2023-07-01 10:06
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('jobapp', '0015_remove_languagelevel_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postjob',
            name='experience',
            field=models.CharField(choices=[('1-3', '1-3'), ('4-6', '4-6'), ('6-9', '6-9'), ('10+', '10 a více')], default='1-3', max_length=100),
        ),
        migrations.AlterField(
            model_name='postjob',
            name='language',
            field=models.CharField(choices=[('NO', 'žádný'), ('ENG1', '🇬🇧 english/beginner'), ('ENG2', '🇬🇧 english/advanced'), ('ENG3', '🇬🇧 english/native speaker'), ('CHF1', '🇨🇭 swiss german/beginner'), ('CHF2', '🇨🇭 swiss german/advanced'), ('CHF3', '🇨🇭 swiss german/native speaker'), ('DEU1', '🇩🇪 germany/beginner'), ('DEU2', '🇩🇪 germany/advanced'), ('DEU3', '🇩🇪 germany/native speaker'), ('FRA1', '🇫🇷 french/beginner'), ('FRA2', '🇫🇷 french/advanced'), ('FRA3', '🇫🇷 french/native speaker'), ('ITA1', '🇮🇹 italy/beginner'), ('ITA2', '🇮🇹 italy/advanced'), ('ITA3', '🇮🇹 italy/native speaker')], default='NO', max_length=100),
        ),
    ]
